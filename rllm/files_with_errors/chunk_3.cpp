#include <iostream>
#include <cstring>
void vulnerable_function(char* input) { // copies the content of the input character pointer into a character array of size 10 using the strcpy function }
int main() {
    char input[10];
    std::cout << "Enter a string: ";
    std::cin >> input;
    vulnerable_function(input);
    std::cout << "The string is: " << input << std::endl;
    return 0;
}