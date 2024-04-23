#include <iostream>
#include <cstring>
void function1(char* input) { // copies the content of the input character pointer into a character array buffer of size 5 using the strcpy function
    char buffer[5];
    strcpy(buffer, input);
    std::cout << buffer << std::endl;
}
int main() {
    char input[5];
    std::cout << "Enter a string: ";
    std::cin >> input;
    function1(input);
    return 0;
}