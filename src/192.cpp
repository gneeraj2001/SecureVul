#include <iostream>
#include <string.h>
void func(char* input) { // Copy the content of the input character pointer into the buffer
    char buffer[100];
    strcpy(buffer, input);
    buffer[strlen(buffer) - 1] = '\0';
    std::cout << buffer << std::endl;
}
int main() {
    char input[100];
    std::cout << "Enter the string: ";
    std::cin >> input;
    func(input);
    return 0;
}