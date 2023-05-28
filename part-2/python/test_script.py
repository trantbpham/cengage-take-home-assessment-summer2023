import unittest
import io

import program_1_test
import program_2_test
import program_3_test

class Test:

    # Constructor for each program
    def __init__(self, program):
        self.program_name = program.__name__
        self.suite = unittest.TestLoader().loadTestsFromModule(program)
        self.total_tests = 0
        self.failed_tests = 0
        self.passed_tests = 0
        
    # This method runs the test for the tester
    def run_test(self):
        out = io.StringIO()
        print()
        print("---------------------------------------------------")
        print("Testing:", self.program_name, "\n")
        result_list = []
        failed_descriptions = {}
        
        # For each of the test cases, get its result
        for test_cases in self.suite:
            for test in test_cases:
                test_result = unittest.TextTestRunner(out, verbosity=2).run(test)
                result_list.append(test._testMethodName)
                self.total_tests += 1

                # Test passed
                if test_result.wasSuccessful():
                    result_list.append("Passed")
                    self.passed_tests += 1
                # Test failed
                else:
                    result_list.append("Failed")
                    failed_descriptions[test._testMethodName] = test_result.failures
                    self.failed_tests += 1
        print()

        # Print each of the method name and its results
        for i in range(0, len(result_list), 2):
            print(result_list[i])
            print(result_list[i+1])
            # If the test failed, display why it failed
            if(result_list[i+1] == "Failed"):
                print(failed_descriptions[result_list[i]])
            print()

        # Print the test summary
        print("-------TEST SUMMARY-------")
        print("Total tests:", self.total_tests)
        print("Failed:", self.failed_tests)
        print("Passed:", self.passed_tests)

        # If all the test cases passed
        if self.failed_tests == 0:
            print()
            print("All tests passed")
        print()

# main program
if __name__ == '__main__':    
    program1 = Test(program_1_test)
    program2 = Test(program_2_test)
    program3 = Test(program_3_test)

    program1.run_test()
    program2.run_test()
    program3.run_test()
