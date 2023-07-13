from contextlib import redirect_stdout
from io import StringIO
import unittest
import python_1_2

class Python_1_2_Tests(unittest.TestCase):

    def setUp(self):
       self.ex = python_1_2.Python_1_2()

    def test_getMessage(self):
        message = "test"
        with redirect_stdout(StringIO()) as output:
           self.ex.print_message(message)
        self.assertEqual(output.getvalue().strip(), message)

    def test_multiplyPositive(self):
        self.assertEqual(self.ex.multiply_numbers(200, 200.00), 40000)

    def test_multiplyPositiveNegative(self):
        self.assertEqual(self.ex.multiply_numbers(200, -200.00), -40000)

    def test_multiplyNegative(self):
        self.assertEqual(self.ex.multiply_numbers(-200, -200.00), 40000)

    def test_multiplyZero(self):
        self.assertEqual(self.ex.multiply_numbers(-200, 0.00), 0)
    
    def test_multiplyString(self):
        self.assertEqual(self.ex.multiply_numbers(2, 200.00), 400)
    
    def test_multiplyError1(self):
        self.assertEqual(self.ex.multiply_numbers(int("a"), 200.00), 400)

    def test_multiplyError2(self):
        self.assertEqual(self.ex.multiply_numbers(2, float("c")), 400)
       
    
if __name__ == '__main__':
    unittest.main()