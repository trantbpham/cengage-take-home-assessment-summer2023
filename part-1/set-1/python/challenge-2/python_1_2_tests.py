import unittest
from unittest.mock import patch
from io import StringIO
from python_1_2 import Python_1_2

class TestPython_1_2(unittest.TestCase):
    def setUp(self):
        self.example = Python_1_2()

    def test_print_message(self):
        message = "Hello, world!"
        expected_output = "Hello, world!"
        with patch('sys.stdout', new=StringIO()) as output: #redirect the output to a StringIO object
            self.example.print_message(message)
            self.assertEqual(output.getvalue().strip(), expected_output)

    def test_multiply_numbers(self):
        num1 = 5
        num2 = 2.5
        expected_output = 12.5
        result = self.example.multiply_numbers(num1, num2)
        self.assertEqual(result, expected_output)

    def test_multiply_numbers_with_integer_input(self):
        num1 = 10
        num2 = 3.5
        expected_output = 35.0
        result = self.example.multiply_numbers(num1, num2)
        self.assertEqual(result, expected_output)

    def test_multiply_numbers_with_float_input(self):
        num1 = 4
        num2 = 1.8
        expected_output = 7.2
        result = self.example.multiply_numbers(num1, num2)
        self.assertEqual(result, expected_output)

    def test_multiply_numbers_with_negative_integer_input(self):
        num1 = -6
        num2 = 2.5
        expected_output = -15.0
        result = self.example.multiply_numbers(num1, num2)
        self.assertEqual(result, expected_output)

    def test_multiply_numbers_with_zero_input_for_num1(self):
        num1 = 0
        num2 = 4.9
        expected_output = 0.0
        result = self.example.multiply_numbers(num1, num2)
        self.assertEqual(result, expected_output)

    def test_multiply_numbers_with_zero_input_for_num2(self):
        num1 = 7
        num2 = 0.0
        expected_output = 0.0
        result = self.example.multiply_numbers(num1, num2)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
