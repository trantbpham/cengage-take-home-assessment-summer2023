import unittest
from io import StringIO
from contextlib import redirect_stdout
from python_1_2 import Python_1_2

# This class tests the methods in python_1_2.py
class Python_1_2_test(unittest.TestCase):

    def setUp(self):
        self.python_example = Python_1_2()

    # This method tests print_message function.
    def test_print_message(self):
        expected_output = "This is a test message\n"
        message = "This is a test message"

        captured_output = StringIO()   
        with redirect_stdout(captured_output):
            self.python_example.print_message(message)

        self.assertEqual(expected_output, captured_output.getvalue())

    # This method tests multiply_numbers function using two positive numbers
    def test_multiply_numbers_1(self):
        expected_output = 20
        num1 = 4
        num2 = 5.0
        result = self.python_example.multiply_numbers(num1, num2)
        self.assertEqual(expected_output, result)

    # This method tests multiply_numbers function using one positive and one negative number.
    def test_multiply_numbers_2(self):
        expected_output = -20
        num1 = -4
        num2 = 5.0
        result = self.python_example.multiply_numbers(num1, num2)
        self.assertEqual(expected_output, result)

    # This method tests multiply_numbers function using two negative numbers.
    def test_multiply_numbers_3(self):
        expected_output = 20
        num1 = -4
        num2 = -5.0
        result = self.python_example.multiply_numbers(num1, num2)
        self.assertEqual(expected_output, result)

    # This method tests multiply_numbers function by multiplying with 0.
    def test_multiply_numbers_4(self):
        expected_output = 0
        num1 = 0
        num2 = 2.4
        result = self.python_example.multiply_numbers(num1, num2)
        self.assertEqual(expected_output, result)

if __name__ == '__main__':
    unittest.main()