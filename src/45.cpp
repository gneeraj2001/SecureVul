#include <iostream>
int main() { // declare a character array named buffer of size 10 and read input into it using cin
    char buffer[10]; // declare a character array of size 10
    std::cout << "Enter a string: ";
    std::cin >> buffer; // read input from cin into buffer
    std::cout << "The string is: " << buffer << std::endl; // print the contents of buffer to the console
    return 0;
}