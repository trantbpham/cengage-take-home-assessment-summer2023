import unittest
from io import StringIO
from unittest.mock import patch

class PythonChallengeOneTest(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def testPrint(self, mock_stdout):
        expected_output = "I am learning to program in Python\nThat's awesome!\n"
        
        import python_1_1
        
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()