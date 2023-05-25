import subprocess
import unittest
import python_1_1
import os

class Python_1_1_Tests(unittest.TestCase):

    def test_print(self):
        proc = subprocess.Popen(['python', python_1_1.__file__], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        self.assertEqual(proc.communicate()[0].decode(), "I am learning to program in Python\r\nThat's awesome!\r\n")

if __name__ == '__main__':
    unittest.main()