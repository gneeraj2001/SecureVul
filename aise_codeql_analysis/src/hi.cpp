/*
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    const char* message = "Hello";
    char buffer[256];
    size_t message_length = strlen(message);
    memcpy(buffer, message, message_length);
    printf("%s\n", buffer);
    return 0;
}
*/
#include <iostream>
#include <cstring>

int main() {
    char buffer[5]; // Buffer with a size of 5 characters
    std::cout << "Enter a string: ";
    std::cin >> buffer; // User input

    // Print the input string
    std::cout << "You entered: " << buffer << std::endl;

    return 0;
}

