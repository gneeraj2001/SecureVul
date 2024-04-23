#include <iostream>
#include <cstring>
void process(char* input) { // Declare a character array buffer of size 10. Copy the content of the input character pointer into the buffer using the strcpy function. Then print out the processed input using cout.
    char buffer[10];
    strcpy(buffer, input);
    std::cout << buffer << std::endl;
}
int main() {
    char input[] = "Hello World";
    process(input);
    return 0;
}