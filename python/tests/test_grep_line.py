import unittest
from src.grep_line import extract

IGNORE_TEST = True
LINES = """
   start-marker
line 1
line 2
   end-marker
line 3
line 4
"""
LINES = LINES.split("\n")
START_MARKER = "start-marker"
END_MARKER = "end-marker"

#############################
# Tests
#############################
class TestFunctions(unittest.TestCase):

    def testExtractPresent(self):
         if IGNORE_TEST:
            return
         text = extract(LINES, START_MARKER, END_MARKER)
         self.assertEqual(len(text), 2)

    def testExtractAbsent(self):
         if IGNORE_TEST:
            return
         text = extract(LINES, "dummy-begin", "dummy-end")
         self.assertEqual(len(text), 0)

    def testExtractFormatError(self):
         if IGNORE_TEST:
               pass
         with self.assertRaises(ValueError):
               _ = extract(LINES, "dummy-start", END_MARKER)
         with self.assertRaises(ValueError):
               _ = extract(LINES, START_MARKER, "dummy-end")



if __name__ == "__main__":
    unittest.main()
