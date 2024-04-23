#include <iostream>
#include <cstring>
void vulnerable_function(char* input) { // copies the content of the input character pointer into a character array of size 10 using the strcpy function } int main() { // declares a character array of size 20 and initializes it with a string "This is a large input". Then calls the vulnerable_function with the large_input as an argument }

int main() {
    char large_input[20];
    strcpy(large_input, "This is a large input");
    vulnerable_function(large_input);
    return 0;
}