#include <iostream>
int main() { // take user input and copy it into a buffer array causing a potential buffer overflow
    char buffer[100];
    std::cout << "Enter a string: ";
    std::cin >> buffer;
    std::cout << "The string is: " << buffer << std::endl;
    return 0;
}