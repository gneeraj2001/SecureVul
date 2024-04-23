#include <iostream>
#include <cstring>
void vulnerableFunction(char* input) { // Copy the input into a buffer using strcpy and print the buffer content using cout }
int main() {
    char input[100];
    std::cout << "Enter the string: ";
    std::cin >> input;
    vulnerableFunction(input);
    std::cout << "The string is: " << input << std::endl;
    return 0;
}