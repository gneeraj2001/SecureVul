#include <iostream>
#include <cstring>
void vulnerableFunction(char* input) { // copies the content of the input into the buffer using the strcpy function
    strcpy(input, "Hello World");
}
int main() {
    char input[100];
    vulnerableFunction(input);
    std::cout << input << std::endl;
}