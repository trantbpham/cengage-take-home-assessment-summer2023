// Program: Challenge2 (C++)
// Description: Demonstrates a class with functions that interact with console input

#include <iostream>
#include <string>

class ChallengeTwo {
public:
    void printMessage(const std::string& message) {
        std::cout << message << std::endl;
    }

    double multiplyNumbers(int num1, double num2) {
        return num1 * num2;
    }
};

int main() {
    ChallengeTwo challengeTwo;

    std::string message;
    std::cout << "Enter a message: ";
    std::getline(std::cin, message);
    challengeTwo.printMessage(message);

    int num1;
    double num2;
    std::cout << "Enter an integer: ";
    std::cin >> num1;
    std::cout << "Enter a double: ";
    std::cin >> num2;
    double result = challengeTwo.multiplyNumbers(num1, num2);
    std::cout << "The multiplication result is: " << result << std::endl;

    return 0;
}
