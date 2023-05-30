import unittest
from io import StringIO
from contextlib import redirect_stdout

import program_1
import program_2
import program_3
import program_tests
import program2_tests
import program3_tests


def run_test_suite():
    # Load test cases
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Testing program_test file
    suite.addTests(loader.loadTestsFromModule(program_tests))

    # Testing Testing program_2 file
    suite.addTests(loader.loadTestsFromModule(program2_tests))

    # Testing program_3 file
    suite.addTests(loader.loadTestsFromModule(program3_tests))

    # Run the test suite
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    # Print test results
    print("Test Results:")
    for failure in result.failures:
        print(f"Failure: {failure[0]} - {failure[1]}")

    print(f"Total Tests Run: {result.testsRun}")
    print(f"Total Test Cases Passed: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Total Test Cases Failed: {len(result.failures)}")
   


if __name__ == '__main__':
    run_test_suite()

