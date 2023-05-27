import unittest
import io
import sys
import contextlib
import python_1_2

# Note: a couple of the tests fail, commented where needed
class PythonSet1Challenge2Test(unittest.TestCase):

    def test_print_message(self):
        expected = "This is a message"
        self.test_print_message_helper(expected)
    
    def test_print_message_empty(self):
        self.test_print_message_helper()
        

    def test_print_message_empty_none(self):
        self.test_print_message_helper("None", None)

    def test_print_message_number(self):
        self.test_print_message_helper("1.2", 1.2)

    def test_multiply_numbers(self):
        instance = python_1_2.Python_1_2()

        # multiply by 0
        self.assertEqual(0, instance.multiply_numbers(0, 0))
        self.assertEqual(0, instance.multiply_numbers(0, 100))

        # multiply by negative
        self.assertEqual(-270.6, instance.multiply_numbers(3, -90.2))
        self.assertEqual(-270.6, instance.multiply_numbers(-3, 90.2))

        self.assertEqual(153729, instance.multiply_numbers(171, 899))
        self.assertEqual(153729.0, instance.multiply_numbers(int(171), float(899)))
        self.assertEqual(7947.9416331, instance.multiply_numbers(91.007, 87.3333))

        # divide
        self.assertEqual(1/3, instance.multiply_numbers(9, 1/27))
        self.assertEqual(-1/2, instance.multiply_numbers(-9, 1/18))

        # multiply by arbitrarilly large numbers
        self.assertEqual(95378247708541418748648, instance.multiply_numbers(15421681351, 6184685413848))
        self.assertEqual(95378247708541418748648, instance.multiply_numbers(int(15421681351), int(6184685413848)))
        self.assertEqual(95378247708541418748648, instance.multiply_numbers(float(15421681351), int(6184685413848))) # fails, does not support large float
        self.assertEqual(95378247708541418748648, instance.multiply_numbers(float(15421681351), float(6184685413848))) # fails, does not support large float

    # helpers
    def test_print_message_helper(self, expected = "", input = None):
        instance = python_1_2.Python_1_2() # create instance
        out = io.StringIO() # capture
        input = input if input else expected # if input is not included assume input is expected
        with contextlib.redirect_stdout(out): # print to out
            instance.print_message(input)
        actual = out.getvalue().strip()
        # print(expected)
        # print(actual)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
