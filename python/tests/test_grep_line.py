import unittest
from src.grep_line import extract

LINES = """
   start-marker
line 1
line 2
   end-marker
line 3
line 4
"""
START_MARKER = "start-marker"
END_MARKER = "end-marker"

#############################
# Tests
#############################
class TestFunctions(unittest.TestCase):

    def testExtract(self):
        text = extract(LINES, START_MARKER, END_MARKER)
        import pdb; pdb.set_trace()

if __name__ == "__main__":
    unittest.main()
