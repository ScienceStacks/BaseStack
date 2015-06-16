" Environment
" Delete trailing blanks
function! DeleteTrailingBlanks ()
  let cur_pos = getpos(".")
  0,$s/ *$//
  call setpos(".", cur_pos)
endfunction

" Read from buffer x
function! ReadFromTmpBufferx ()
  :r /tmp/t.x
endfunction

" Add period at end of a Python doc string
function! AddPeriodToDocString ()
  s/""" /"""/
  s/$/./
endfunction

" Creates a block for debugging by catching an exception
function! CreateDebugBlock ()
  let cur_pos = getpos(".")
  let end_line = string(cur_pos[1])
  let start_line = input("Start line?")
" Indent
  let cmd = ":" . start_line . "," . end_line . "s/^/  /"
" add try
  let cmd = ":" . start_line . "s/$/\r  try:/"
  :execute cmd
  let cmd = ":s/$/\r except BaseException as e:/"
  :execute cmd
  call setpos(".", cur_pos)
endfunction

" Change double quote to single quote
" Does change from input line number to current line.
" If input line number is NULL, then just done for current line
function! ChangeDoubleQuoteToSingleQuote ()
  let cur_pos = getpos(".")
  let end_line = string(cur_pos[1])
  let start_line = input("Start line?")
  if len(start_line) == 0
    let start_line = end_line
  endif
  let md = ":" . start_line . "," . end_line . 's/"/' . "'/g"
  "echo cmd
  :execute cmd
  call setpos(".", cur_pos)
endfunction

" Unindent Python lines
function! UnindentPyLines ()
  let cur_pos = getpos(".")
  let end_line = string(cur_pos[1])
  let start_line = input("Start line?")
  if len(start_line) == 0
    let start_line = end_line
  endif
  let cmd = ":" . start_line . "," . end_line . "s/^  //"
  :execute cmd
  call setpos(".", cur_pos)
endfunction

" Indent Python lines
function! IndentPyLines ()
  let cur_pos = getpos(".")
  let end_line = string(cur_pos[1])
  let start_line = input("Start line?")
  if len(start_line) == 0
    let start_line = end_line
  endif
  let cmd = ":" . start_line . "," . end_line . "s/^/  /"
  :execute cmd
  call setpos(".", cur_pos)
endfunction


" Add period at end of a Python doc string
function! AddPeriodToQuotedDocString ()
  s/""" /"""/
  s/ """$/."""/
  s/ ."""$/."""/
endfunction

" Delete lines
function! DeleteLines ()
  let cur_pos = getpos(".")
  let end_line = string(cur_pos[1])
  let start_line = input("Start line?")
  if len(start_line) == 0
    let start_line = end_line
  endif
  let cmd = ":" . start_line . "," . end_line . 'd'
  :execute cmd
endfunction

" Cut lines, writing them to the external buffer
function! CutLines ()
  let cur_pos = getpos(".")
  let end_line = string(cur_pos[1])
  let start_line = input("Start line?")
  if len(start_line) == 0
    let start_line = end_line
  endif
  let cmd = ":" . start_line . "," . end_line . 'w!/tmp/t.x'
  :execute cmd
  let cmd = ":" . start_line . "," . end_line . 'd'
  :execute cmd
endfunction

" Replace dash
function! ReplaceDashWithColon ()
  s/ - /: /
endfunction

" Equals
function! EliminateBlanksInEquals ()
  s/ = /=/
endfunction

" Equals
function! CopyLinesToBuffer ()
  let cur_pos = getpos(".")
  let end_line = string(cur_pos[1])
  let start_line = input("Start line?")
  if len(start_line) == 0
    let start_line = end_line
  endif
  let cmd = ":" . start_line . "," . end_line . 'w!/tmp/t.x'
  :execute cmd
  call setpos(".", cur_pos)
endfunction

" Change g4 password
function! ChangeP4Password()
  :/P4PASSWD/s/<old pw>/<new pw>/
endfunction

" Constructor assignment
" Intended to be used by copying lines from the argument list of the def
function! BuildPythonConstructorAssignmentLine ()
  :.,.s/ //g
  :.,.s/,$//
  :.,.s/^.*$/    self.& = &/
endfunction

" Make a local variable private
function! MakeAllVariableLocal()
  let line_num = input("Start line?")
  if len(line_num) == 0
    echo "***Must provide a string"
    return
  endif
  let cur_pos = getpos(".")
  let cmd = ":" . line_num . "," . string(cur_pos[1])
  let cmd = cmd . "s/self\\./self.__/g"
  :execute cmd
  call setpos(".", cur_pos)
  ":echo cmd
endfunction

" Change self variables to locals
" Assumes positioned at the end of the class
function! MakeVariableLocal()
  let word = input("Word?")
  if len(word) == 0
    echo "***Must provide a string"
  else
    let cur_pos = getpos(".")
    let cmd = ":0,$s/self." . word . "/self.__" . word . "/g"
    :echo cmd
    :execute cmd
    call setpos(".", cur_pos)
  endif
endfunction

" Swap double quote for single quote
function! SwapDoubleQuoteForSingleQuote()
  let double_quote = '"'
  let cmd = ":s/" . double_quote . "/'/g"
  :execute cmd
endfunction

" Swap windows for case of two windows
let g:current_window = 0
function! SwapWindow()
  let cmd1 = "<C-W>"
  if g:current_window == 0
    let cmd2 = "<right>"
  else
    let cmd2 = "<left>"
  endif
  let g:current_window = 1 - g:current_window
  :execute cmd1
  :execute cmd2
endfunction

" Format argument lines as log lines
" Current pointer should be at the end of the range
function! FormatLogLines()
  let line_num = input("Start line?")
  if len(line_num) == 0
    echo "***Must provide a string"
    return
  endif
  let cur_pos = getpos(".")
  let cmd_range = ":" . line_num . "," . string(cur_pos[1])
  let cmd_trimblanks = "s/^ *//"
  let cmd = cmd_range . cmd_trimblanks
  :execute cmd
  let cmd_trimend = "s/,.*$//"
  let cmd = cmd_range . cmd_trimend
  :execute cmd
  let cmd_trimend = "s/=.*$//"
  let cmd = cmd_range . cmd_trimend
  :execute cmd
  let cmd_trimend = "s/).*$//"
  let cmd = cmd_range . cmd_trimend
  :execute cmd
  let cmd_logline = 's/^.*$/    log_line += " & = " + str(&)/'
  let cmd = cmd_range . cmd_logline
  :execute cmd
  let cmd_newline = "normal $a\n"
  let cmd_newline = cmd_newline . "logging.log(logging.DEBUG, log_line)"
  call setpos(".", cur_pos)
  :execute cmd_newline
endfunction

" assign name as an argument
" e.g. self.name = util.TypeCheck(basestring, name)
function! AssignPyVariable()
  let var_name = input("Variable name?")
  let cmd = ":s/$/\r    self." . var_name . " = " . var_name 
  :execute cmd
endfunction

" insert Py debug
function! InsertPyDebug()
  " let cmd = ":s/$/\r    import pdb; pdb.set_trace()/"
  let cmd = ":s/$/\r    bogus_statement/"
  :execute cmd
endfunction

" Add period to end of line
function! AddPeriodToEndOfLine()
  :.,.s/$/&./
endfunction

" Comment out lines
" Current pointer should be at the end of the range
function! CommentOutLines()
  let cur_pos = getpos(".")
  let line_num = input("Start line?")
  if len(line_num) == 0
    let line_num = string(cur_pos[1])
  endif
  let cmd_range = ":" . line_num . "," . string(cur_pos[1])
  let cmd = cmd_range . "s/^/#mock/"
  :execute cmd
  call setpos(".", cur_pos)
endfunction

" Add ignore for pylint
function PylintIgnore()
    s/$/  # pylint:disable-msg=C6409/
endfunction

" Environment
function! SetEnvironment()
 :hi normal ctermfg=black ctermbg=white
endfunction



nmap ,a :call AssignPyVariable ()<CR>
nmap ,b :call CommentOutLines ()<CR>
nmap ,c :call CopyLinesToBuffer ()<CR>
nmap ,d :call DeleteLines ()<CR>
nmap ,e :call SetEnvironment()<CR>
nmap ,g :call ChangeP4Password ()<CR>
nmap ,i :call IndentPyLines()<CR>
nmap ,l :call MakeAllVariableLocal ()<CR>
nmap ,p :call InsertPyDebug ()<CR>
nmap ,q :call ChangeDoubleQuoteToSingleQuote ()<CR>
nmap ,r :call ReadFromTmpBufferx ()<CR>
nmap ,s :call SwapDoubleQuoteForSingleQuote () <CR>
nmap ,t :call FormatLogLines ()<CR>
nmap ,u :call UnindentPyLines () <CR>
nmap ,x :call CutLines () <CR>

nmap ,,dc :call CreateDebugBlock() <CR>

:call SetEnvironment()
:call SetEnvironment()

:set statusline=%t\ %y\ format:\ %{&ff};\ [%c,%l]
:set laststatus=2
:set nu
