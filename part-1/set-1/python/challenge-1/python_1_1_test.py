import unittest
from io import StringIO
from contextlib import redirect_stdout

# This class tests the print statements in python_1_1.py
class Python_1_1_test(unittest.TestCase):

    def test_print(self):
        expected_output = "I am learning to program in Python\nThat's awesome!\n"
        captured_output = StringIO()                 
        with redirect_stdout(captured_output):
            import python_1_1
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()