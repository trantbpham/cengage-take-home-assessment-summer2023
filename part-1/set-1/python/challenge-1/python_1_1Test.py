import sys
import unittest
from io import StringIO


class MyTestCase(unittest.TestCase):
    def test_print_statements(self):

        # StringIO object used to capture the output
        output = StringIO() 

        # Redirect standard output to StringIO object
        sys.stdout = output  

        # Executing print statements as given in program
        print("I am learning to program in Python")
        print("That's awesome!")

        # Resetting stdout
        sys.stdout = sys.__stdout__  

        # Storing output
        answer = output.getvalue().strip()

        self.assertEqual(answer, "I am learning to program in Python\nThat's awesome!")
        


if __name__ == '__main__':
    unittest.main()
