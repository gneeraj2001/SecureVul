#include <iostream>
#include <string.h>
void vulnerableFunction(char* input) { // Copy the input character array into a buffer and print the buffer content.
    char buffer[100];
    strcpy(buffer, input);
    std::cout << buffer << std::endl;
}

int main() {
    char input[] = "Hello World!";
    vulnerableFunction(input);
    return 0;
}