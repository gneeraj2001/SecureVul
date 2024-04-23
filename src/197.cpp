#include <iostream>
#include <string.h>
void func(char* input) { // Copy the content of the input character pointer into the buffer
    char buffer[100];
    strcpy(buffer, input);
    std::cout << buffer << std::endl;
}
int main() {
    char input[] = "Hello World";
    func(input);
    return 0;
}