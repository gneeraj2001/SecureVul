#include <iostream>
#include <cstring>
void vulnerableFunction(char* input) { // create a buffer of size 10 characters, copy the content of the user input into the buffer using strcpy, and then print the buffer to the console
    char buffer[10];
    strcpy(buffer, input);
    std::cout << buffer << std::endl;
}
int main() {
    char input[10];
    std::cout << "Enter a string: ";
    std::cin >> input;
    vulnerableFunction(input);
    return 0;
}