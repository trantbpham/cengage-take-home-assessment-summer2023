import unittest
from io import StringIO
from contextlib import redirect_stdout

# Dynamically load the programs
import program_1_test
import program_2_test
import program_3_test


def run_tests(program_module):
    # Load the test cases
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromModule(program_module))

    # Run the tests
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    # Build the test results dictionary
    test_results = {
        "total_tests": result.testsRun,
        "passed": result.testsRun - len(result.failures) - len(result.errors),
        "failed": len(result.failures) + len(result.errors),
        "failures": [],
        "errors": []
    }

    # Add details of failed test cases
    for failure in result.failures:
        test_results["failures"].append({
            "test_case": str(failure[0]),
            "reason": str(failure[1])
        })

    # Add details of test errors
    for error in result.errors:
        test_results["errors"].append({
            "test_case": str(error[0]),
            "reason": str(error[1])
        })

    return test_results


# Run the tests for each program and store the results
program_results = {}

# Run the tests for program 1
program_results["program_1"] = run_tests(program_1_test)

# Run the tests for program 2
program_results["program_2"] = run_tests(program_2_test)

# Run the tests for program 3
program_results["program_3"] = run_tests(program_3_test)


# Print the test results for each program -> 
# By using this mechanism, we can identify which program file has failed and why, 
# as the script provides a clear breakdown of the test results for each program
for program_name, results in program_results.items():
    print(f"Test Results for {program_name}:")
    print(f"Total Tests: {results['total_tests']}")
    print(f"Passed: {results['passed']}")
    print(f"Failed: {results['failed']}\n")

    if results["failures"] or results["errors"]:
        print("Failed Test Cases:")
        for failure in results["failures"]:
            print(f"Test Case: {failure['test_case']}")
            print(f"Reason: {failure['reason']}")
            print()
        for error in results["errors"]:
            print(f"Test Case: {error['test_case']}")
            print(f"Reason: {error['reason']}")
            print()