#include <iostream>
#include <cstring>
void vulnerableFunction(char* input) { // Copy the content of the input character pointer into a buffer and print it using cout
    char buffer[100];
    strcpy(buffer, input);
    std::cout << buffer << std::endl;
}

int main() {
    char input[100];
    std::cout << "Enter a string: ";
    std::cin >> input;
    vulnerableFunction(input);
    return 0;
}