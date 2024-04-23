#include <iostream>
#include <cstring>
void function1(char* input) { // copies the content of the input character pointer into a buffer array using the strcpy function.
    char buffer[100];
    strcpy(buffer, input);
    std::cout << buffer << std::endl;
}
int main() {
    char input[] = "Hello World";
    function1(input);
    return 0;
}