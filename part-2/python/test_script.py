import unittest

import program_1
import program_2
import program_3
import program_tests

def warp_test_suite(testcase_class):
    """Load tests from a specific set of TestCase classes."""
    suite = unittest.TestSuite()
    tests = unittest.defaultTestLoader.loadTestsFromTestCase(testcase_class)
    suite.addTest(tests)
    return suite

if __name__ == '__main__':    
    suite = unittest.TestLoader().loadTestsFromModule(program_tests)
    testResult = unittest.TextTestRunner().run(suite)

    if len(testResult.failures) == 0:
        print("All tests passed")
    else:
        print("Total tests:", testResult.testsRun)
        print("Failed:", len(testResult.failures))
        print("Passed:", testResult.testsRun-len(testResult.failures))
