# Program: Console Input Example (Python)
# Description: Demonstrates a class with functions that interact with console input

class Python_1_2:
    def print_message(self, message):
        print(message)

    def multiply_numbers(self, num1, num2):
        return num1 * num2

if __name__ == '__main__':
    example = Python_1_2()

    message = input("Enter a message: ")
    example.print_message(message)

    num1 = int(input("Enter an integer: "))
    num2 = float(input("Enter a double: "))
    result = example.multiply_numbers(num1, num2)
    print("The multiplication result is:", result)
