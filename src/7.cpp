#include <iostream>
#include <cstring>
void vulnerableFunction(char* input) { // create a buffer of size 10 characters, copy the content of the user input into the buffer using strcpy, and then print the buffer to the console
    strcpy(input, "Hello World"); // copy the content of the user input into the buffer using strcpy
    std::cout << input << std::endl; // print the buffer to the console
}
int main() {
    char input[10]; // create a buffer of size 10 characters
    vulnerableFunction(input); // call the vulnerable function
    return 0;
}