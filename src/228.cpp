#include <iostream>
#include <cstring>
void func(char* input_str) { // Copy the content of the input string into the buffer using strcpy and print out the copied string
    strcpy(input_str, "Hello World");
    std::cout << input_str << std::endl;
}

int main() {
    char input_str[100];
    func(input_str);
    return 0;
}