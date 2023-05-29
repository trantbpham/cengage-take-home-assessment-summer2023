import unittest
from io import StringIO
from unittest.mock import patch
from python_1_2 import Python_1_2

class PythonChallenge2Test(unittest.TestCase):

    def setUp(self):
        self.instance = Python_1_2()
        
        
    def test_print_message(self):
        expected_output = "Testing 1,2,3\n"
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.instance.print_message("Testing 1,2,3")
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_print_message_empty(self):
        expected_output = "\n"
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.instance.print_message("")
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_multiply_numbers(self):
        # Test multiplication with positive numbers
        expected_result = 10
        result = self.instance.multiply_numbers(4, 2.5)
        self.assertEqual(result, expected_result)

        # Test multiplication with zero values
        expected_result = 0
        result = self.instance.multiply_numbers(0, 0)
        self.assertEqual(result, expected_result)

        # Test multiplication with negative values
        expected_result = -5
        result = self.instance.multiply_numbers(-2, 2.5)
        self.assertEqual(result, expected_result)

        # Test multiplication with fractions
        expected_result = 6
        result = self.instance.multiply_numbers(3, 4/2)
        self.assertEqual(result, expected_result)

        # Test multiplication with large values
        expected_result = float('85819755394891981944260')
        result = self.instance.multiply_numbers(int('566344913524'), float('151532667365'))
        self.assertEqual(result, expected_result)

        # Test multiplication with max values
        expected_result = float('inf')
        result = self.instance.multiply_numbers(float('inf'), float('inf'))
        self.assertEqual(result, expected_result)

    ## Running Script Tests ##
    # Test script with valid mock inputs.
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_script_execution(self, mock_stdout, mock_input):
        mock_input.side_effect = ["Test message", "4", "2.5"]

        script = Python_1_2()

        script.print_message(input("Enter a message: "))
        result = script.multiply_numbers(
            int(input("Enter an integer: ")),
            float(input("Enter a double: "))
        )
        
        print("The multiplication result is:", result)

        expected_output = "Test message\nThe multiplication result is: 10.0\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        
    ## Test Divide Numbers with running script.
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_script_divide(self, mock_stdout, mock_input):
        mock_input.side_effect = ["Test divide", "1", "3/2"]

        script = Python_1_2()

        script.print_message(input("Enter a message: "))
        result = script.multiply_numbers(
            int(input("Enter an integer: ")),
            float(input("Enter a double: "))
        )
        
        print("The multiplication result is:", result)

        expected_output = "Test divide\nThe multiplication result is: 1.5\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)
        # FAILS. Cannot use a fraction in multiply_numbers when script runs.
        # Can be solved using eval(input("")) instead of float, but not ideal.
        # Can validate inputs and throw error instead.
            
            
    ### ERROR Testing ###            
    def test_multiply_numbers_type_error(self):
        with self.assertRaises(TypeError):
            self.instance.multiply_numbers("4", 2.5)
        
    ## Test Error for non-integer input during script excecution.
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_script_non_integer_error(self, mock_stdout, mock_input):
        mock_input.side_effect = ["Test non-int", "non-int", "2.5"]

        script = Python_1_2()
        script.print_message(input("Enter a message: "))

        with self.assertRaises(ValueError) as cm:
            script.multiply_numbers(
                int(input("Enter an integer: ")),
                float(input("Enter a double: "))
            )

        expected_output = "Test non-int\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

        expected_error = "invalid literal for int() with base 10: 'non-int'"
        self.assertIn(expected_error, str(cm.exception))
        
    ## Test Error for using a fraction in float input.
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_script_divide_error(self, mock_stdout, mock_input):
        mock_input.side_effect = ["Test divide", "1", "3/2"]

        script = Python_1_2()
        script.print_message(input("Enter a message: "))

        with self.assertRaises(ValueError) as cm:
            script.multiply_numbers(
                int(input("Enter an integer: ")),
                float(input("Enter a double: "))
            )
        
        print("The multiplication result is: 1.5")        

        expected_output = "Test divide\nThe multiplication result is: 1.5\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

        expected_error = "could not convert string to float: '3/2'"
        self.assertIn(expected_error, str(cm.exception))
        
if __name__ == '__main__':
    unittest.main()
