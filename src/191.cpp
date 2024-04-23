#include <iostream>
#include <cstring>
void print_name(char* input) { // declare a character array named buffer of size 10 and copy the content of the input character pointer into the buffer using strcpy. Then print "Hello, " followed by the content of the buffer.
    char buffer[10];
    strcpy(buffer, input);
    std::cout << "Hello, " << buffer << std::endl;
}
int main() {
    char input[10];
    std::cout << "Enter your name: ";
    std::cin >> input;
    print_name(input);
    return 0;
}