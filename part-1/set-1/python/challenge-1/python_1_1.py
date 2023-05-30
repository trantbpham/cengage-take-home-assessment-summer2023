# Program: Learning to program message
# Description: Prints two messages to the console using Python

print("I am learning to program in Python")
print("That's awesome!")



# TEST CASES
def test_program_output():
    # Test Case 1: Check Message Content
    expected_output = "I am learning to program in Python\nThat's awesome!\n"
    output = run_program()
    assert output == expected_output, "Failed Test Case 1: Incorrect message content"

    # Test Case 2: Check Message Order
    expected_output = "I am learning to program in Python\nThat's awesome!\n"
    output = run_program()
    assert output == expected_output, "Failed Test Case 2: Incorrect message order"

    # Test Case 3: Non-empty Output
    expected_output = "I am learning to program in Python\nThat's awesome!\n"
    output = run_program()
    assert output != "", "Failed Test Case 3: Program should produce non-empty output"
    assert output == expected_output, "Failed Test Case 3: Incorrect output"


def run_program():
    # Run the program and capture the output
    import sys
    from io import StringIO

    original_stdout = sys.stdout
    sys.stdout = captured_output = StringIO() # capture the output and redirect to StringIO object

    # Insert the program code here
    print("I am learning to program in Python")
    print("That's awesome!")

    sys.stdout = original_stdout
    return captured_output.getvalue()


if __name__ == '__main__':
    try:
        # Run the test function
        test_program_output()
    except AssertionError:
        raise
    print()
    print('ALL TESTS PASSED!')

