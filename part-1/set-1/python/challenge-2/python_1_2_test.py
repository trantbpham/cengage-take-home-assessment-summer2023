import unittest
from io import StringIO
from unittest.mock import patch
from python_1_2 import Python_1_2

class PythonChallengeTwoTest(unittest.TestCase):

    def setUp(self):
        self.example = Python_1_2()

    @patch('sys.stdout', new_callable=StringIO)
    def testPrintMessage(self, mock_stdout):
        message = "Test message"
        expected_output = "Test message\n"

        self.example.print_message(message)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def testMultiplyNumbers(self):
        num1 = 6
        num2 = 4
        expected_result = 24

        result = self.example.multiply_numbers(num1, num2)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
