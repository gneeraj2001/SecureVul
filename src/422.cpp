#include <iostream>
#include <cstring>
void vulnerableFunction(char* input) { // Copy the content of the input character array into the buffer using the strcpy function.
    strcpy(input, "Hello World");
}

int main() {
    char input[100];
    vulnerableFunction(input);
    std::cout << input << std::endl;
    return 0;
}