#include <iostream>
#include <cstring>
void func(char* input) { // Copy the content of the input character pointer into the buffer using the strcpy function and print out the contents of the buffer.
    strcpy(input, "Hello World!");
}
int main() {
    char input[100];
    func(input);
    std::cout << input << std::endl;
    return 0;
}