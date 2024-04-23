#include <iostream>
#include <string>
int main() { // take a string input from the user and copy it into another string, truncating if necessary
    std::string input;
    std::cout << "Enter a string: ";
    std::cin >> input;
    std::string output;
    if (input.length() > 10) {
        output = input.substr(0, 10);
    } else {
        output = input;
    }
    std::cout << output << std::endl;
    return 0;
}