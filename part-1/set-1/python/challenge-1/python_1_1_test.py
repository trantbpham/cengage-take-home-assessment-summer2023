import unittest
import io
import sys

class PythonSet1Challenge1Test(unittest.TestCase):
    def testStdOut(self):
        expected = "I am learning to program in Python\nThat's awesome!\n"
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput # set out to capture object
        import python_1_1 # run file
        actual = capturedOutput.getvalue()
        self.assertEqual(expected, actual)
        sys.stdout = sys.__stdout__ # set back

if __name__ == '__main__':
    unittest.main()
