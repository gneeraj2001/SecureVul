#include <iostream>
#include <cstring>
void vulnerable_function(char* input) { // Declare a buffer array of size 10 and copy input into buffer using strcpy. Print buffer content using cout.
    char buffer[10];
    strcpy(buffer, input);
    std::cout << buffer << std::endl;
}

int main() {
    char input[] = "Hello World";
    vulnerable_function(input);
    return 0;
}