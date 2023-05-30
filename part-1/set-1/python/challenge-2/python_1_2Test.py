import unittest
from io import StringIO
from unittest.mock import patch
from python_1_2 import Python_1_2


class MyTestCase(unittest.TestCase):
    
    def test_multiplication(self):

        python_obj = Python_1_2()

        value1 = 32
        value2 = 3.8
        expected_output = 121.6

        actual_output = python_obj.multiply_numbers(value1, value2)

        self.assertEqual(actual_output, expected_output)

    def test_multiplicationWithZero(self):

        python_obj = Python_1_2()

        value1 = 0
        value2 = 34.2
        expected_output = 0.0

        actual_output = python_obj.multiply_numbers(value1, value2)

        self.assertEqual(actual_output, expected_output)

    def test_multiplicationWithNegativeNumber(self):

        python_obj = Python_1_2()

        value1 = -40
        value2 = -3
        expected_output = 120.0

        actual_output = python_obj.multiply_numbers(value1, value2)

        self.assertEqual(actual_output, expected_output)

    def test_multiplicationWithLargeNumber(self):

        python_obj = Python_1_2()

        value1 = 1000000
        value2 = 17.5456989
        expected_output = 17545698.9

        actual_output = python_obj.multiply_numbers(value1, value2)

        self.assertAlmostEqual(actual_output, expected_output, places=2)

    def test_printMessage(self):

        python_obj = Python_1_2()

        expected_output = "Hello, World!"

        with patch("sys.stdout", new=StringIO()) as simulated_stdout:
            python_obj.print_message(expected_output)
            output = simulated_stdout.getvalue().strip()

        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
