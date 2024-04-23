#include <iostream>
#include <cstring>
void function1(char* input) { // copies the content of the input character pointer into a buffer array using the strcpy function
    strcpy(buffer, input);
}
int main() {
    char input[100];
    std::cout << "Enter a string: ";
    std::cin >> input;
    function1(input);
    std::cout << "The string is: " << buffer << std::endl;
    return 0;
}