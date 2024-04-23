#include <iostream>
#include <cstring>
void func(char* input_str) { // Declare a character array buffer of size 10. Copy the content of input string into buffer using strcpy. Print out the copied string to the console.
    char buffer[10];
    strcpy(buffer, input_str);
    std::cout << buffer << std::endl;
}

int main() {
    char input_str[] = "Hello World!";
    func(input_str);
    return 0;
}