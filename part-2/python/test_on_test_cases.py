import program_tests, program_tests_2, program_tests_3
import unittest
import io

# TestAnalysis class for running analysis on test class, see run_analysis(),
# and printing the report, see print_report()
#
# Note: I did not see any tests for program_2 or program_3 so I made copies of program_tests
# and created new test files, see program_tests_2.py and program_tests_3.py
# these files are identical to program_tests.py, just replacing program_1 with program_{#}

class TestAnalysis:
    def __init__(self, program, title):
        self.name = program.__name__
        self.results = []
        self.suite = unittest.TestLoader.loadTestsFromModule(unittest.TestLoader(), program)
        self.title = title
        self.total_test_count = 0
        self.total_test_fails = 0
        self.total_test_classes = 0

    def run_analysis(self):
        for test_class in self.suite:
            for test in test_class:
                out = io.StringIO() # capture stdout in run
                result = unittest.TextTestRunner(out, verbosity=3).run(test) # run single test

                # store results in dictionary and append to results array
                result_dict = {}
                result_dict['result'] = result
                result_dict['test_case_name'] = test._testMethodName
                self.results.append(result_dict)

                # increment counts
                if not result.wasSuccessful():
                    self.total_test_fails += 1
                self.total_test_count += 1
            self.total_test_classes += 1

    def print_report(self):
        print("\n----------------------------------------------------------------------")
        print("START")
        print("----------------------------------------------------------------------")
        print("Results for " + self.name)
        print("  Total tests: " + str(self.total_test_count))
        print("  Fails: " + str(self.total_test_fails))
        print("  Successes: " + str(self.total_test_count - self.total_test_fails))
        print("----------------------------------------------------------------------")
        for result in self.results:
            print(result['test_case_name'])
            if not result['result'].wasSuccessful():
                print("  test failed, report below:")
                print("\n----------------------------------------------------------------------")
                for failure in result['result'].failures:
                    for item in failure:
                        print(item)
                print("----------------------------------------------------------------------\n")
            else:
                print("  test passed")
            print()
        print("----------------------------------------------------------------------")
        print("END")
        print("----------------------------------------------------------------------\n")


if __name__ == '__main__':
    results_program_1 = TestAnalysis(program_tests, "Program 1")
    results_program_2 = TestAnalysis(program_tests_2, "Program 2")
    results_program_3 = TestAnalysis(program_tests_3, "Program 3")
    results_program_1.run_analysis()
    results_program_1.print_report()
    results_program_2.run_analysis()
    results_program_2.print_report()
    results_program_3.run_analysis()
    results_program_3.print_report()