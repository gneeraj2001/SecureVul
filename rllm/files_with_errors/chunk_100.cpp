#include <iostream>
#include <string.h>
void vulnerable_function(char* input) { // Copy the input to a buffer using strcpy and print the buffer content }
int main() {
    char input[100];
    strcpy(input, "Hello World");
    vulnerable_function(input);
    return 0;
}