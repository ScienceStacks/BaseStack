import inspect

try:
    import trace
except ImportError:
    pass
else:
    trace._warn = lambda *args: None   # workaround for http://bugs.python.org/issue17143 (PY-8706)

import gc
from _pydevd_bundle.pydevd_comm import CMD_SIGNATURE_CALL_TRACE, NetCommand
from _pydevd_bundle import pydevd_vars
from _pydevd_bundle.pydevd_constants import xrange, dict_iter_items
from _pydevd_bundle import pydevd_utils

class Signature(object):
    def __init__(self, file, name):
        self.file = file
        self.name = name
        self.args = []
        self.args_str = []
        self.return_type = None

    def add_arg(self, name, type):
        self.args.append((name, type))
        self.args_str.append("%s:%s"%(name, type))

    def set_args(self, frame, recursive=False):
        self.args = []

        code = frame.f_code
        locals = frame.f_locals

        for i in xrange(0, code.co_argcount):
            name = code.co_varnames[i]
            class_name = get_type_of_value(locals[name], recursive=recursive)

            self.add_arg(name, class_name)

    def __str__(self):
        return "%s %s(%s)"%(self.file, self.name, ", ".join(self.args_str))


def get_type_of_value(value, ignore_module_name=('__main__', '__builtin__', 'builtins'), recursive=False):
    tp = type(value)
    class_name = tp.__name__
    if class_name == 'instance':  # old-style classes
        tp = value.__class__
        class_name = tp.__name__

    if hasattr(tp, '__module__') and tp.__module__ and tp.__module__ not in ignore_module_name:
        class_name = "%s.%s"%(tp.__module__, class_name)

    if class_name == 'list':
        class_name = 'List'
        if len(value) > 0 and recursive:
            class_name += '[%s]' % get_type_of_value(value[0], recursive=recursive)
        return class_name

    if class_name == 'dict':
        class_name = 'Dict'
        if len(value) > 0 and recursive:
            for (k, v) in dict_iter_items(value):
                class_name += '[%s, %s]' % (get_type_of_value(k, recursive=recursive), 
                                            get_type_of_value(v, recursive=recursive))
                break
        return class_name

    if class_name == 'tuple':
        class_name = 'Tuple'
        if len(value) > 0 and recursive:
            class_name += '['
            class_name += ', '.join(get_type_of_value(v, recursive=recursive) for v in value)
            class_name += ']'

    return class_name


class SignatureFactory(object):
    def __init__(self):
        self._caller_cache = {}
        self.cache = CallSignatureCache()

    def is_in_scope(self, filename):
        return not pydevd_utils.not_in_project_roots(filename)

    def create_signature(self, frame, with_args=True):
        try:
            filename, modulename, funcname = self.file_module_function_of(frame)
            signature = Signature(filename, funcname)
            if with_args:
                signature.set_args(frame, recursive=True)
            return signature
        except:
            import traceback
            traceback.print_exc()


    def file_module_function_of(self, frame): #this code is take from trace module and fixed to work with new-style classes
        code = frame.f_code
        filename = code.co_filename
        if filename:
            modulename = trace.modname(filename)
        else:
            modulename = None

        funcname = code.co_name
        clsname = None
        if code in self._caller_cache:
            if self._caller_cache[code] is not None:
                clsname = self._caller_cache[code]
        else:
            self._caller_cache[code] = None
            ## use of gc.get_referrers() was suggested by Michael Hudson
            # all functions which refer to this code object
            funcs = [f for f in gc.get_referrers(code)
                     if inspect.isfunction(f)]
            # require len(func) == 1 to avoid ambiguity caused by calls to
            # new.function(): "In the face of ambiguity, refuse the
            # temptation to guess."
            if len(funcs) == 1:
                dicts = [d for d in gc.get_referrers(funcs[0])
                         if isinstance(d, dict)]
                if len(dicts) == 1:
                    classes = [c for c in gc.get_referrers(dicts[0])
                               if hasattr(c, "__bases__") or inspect.isclass(c)]
                elif len(dicts) > 1:   #new-style classes
                    classes = [c for c in gc.get_referrers(dicts[1])
                               if hasattr(c, "__bases__") or inspect.isclass(c)]
                else:
                    classes = []

                if len(classes) == 1:
                    # ditto for new.classobj()
                    clsname = classes[0].__name__
                    # cache the result - assumption is that new.* is
                    # not called later to disturb this relationship
                    # _caller_cache could be flushed if functions in
                    # the new module get called.
                    self._caller_cache[code] = clsname


        if clsname is not None:
            funcname = "%s.%s" % (clsname, funcname)

        return filename, modulename, funcname


def get_signature_info(signature):
    return signature.file, signature.name, ' '.join([arg[1] for arg in signature.args])


def get_frame_info(frame):
    co = frame.f_code
    return co.co_name, frame.f_lineno, co.co_filename


class CallSignatureCache(object):
    def __init__(self):
        self.cache = {}

    def add(self, signature):
        filename, name, args_type = get_signature_info(signature)
        calls_from_file = self.cache.setdefault(filename, {})
        name_calls = calls_from_file.setdefault(name, {})
        name_calls[args_type] = None

    def is_in_cache(self, signature):
        filename, name, args_type = get_signature_info(signature)
        if args_type in self.cache.get(filename, {}).get(name, {}):
            return True
        return False


def create_signature_message(signature):
    cmdTextList = ["<xml>"]

    cmdTextList.append('<call_signature file="%s" name="%s">' % (pydevd_vars.make_valid_xml_value(signature.file), pydevd_vars.make_valid_xml_value(signature.name)))

    for arg in signature.args:
        cmdTextList.append('<arg name="%s" type="%s"></arg>' % (pydevd_vars.make_valid_xml_value(arg[0]), pydevd_vars.make_valid_xml_value(arg[1])))
        
    if signature.return_type is not None:
        cmdTextList.append('<return type="%s"></return>' % (pydevd_vars.make_valid_xml_value(signature.return_type)))

    cmdTextList.append("</call_signature></xml>")
    cmdText = ''.join(cmdTextList)
    return NetCommand(CMD_SIGNATURE_CALL_TRACE, 0, cmdText)


def send_signature_call_trace(dbg, frame, filename):
    if dbg.signature_factory and dbg.signature_factory.is_in_scope(filename):
        signature = dbg.signature_factory.create_signature(frame)
        if dbg.signature_factory.cache is not None:
            if not dbg.signature_factory.cache.is_in_cache(signature):
                dbg.signature_factory.cache.add(signature)
                dbg.writer.add_command(create_signature_message(signature))
                return True
            else:
                # we don't send signature if it is cached
                return False
        else:
            dbg.writer.add_command(create_signature_message(signature))
            return True
    return False


def send_signature_return_trace(dbg, frame, filename, return_value):
    if dbg.signature_factory and dbg.signature_factory.is_in_scope(filename):
        signature = dbg.signature_factory.create_signature(frame, with_args=False)
        signature.return_type = get_type_of_value(return_value, recursive=True)
        dbg.writer.add_command(create_signature_message(signature))
        return True

    return False



