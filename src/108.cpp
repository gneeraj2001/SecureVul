#include <iostream>
#include <cstring>
void foo(char* input_str) { // copies the content of the input string into a buffer using the strcpy function
    strcpy(input_str, "Hello World"); // copies the content of the input string into a buffer using the strcpy function
}

int main() {
    char input_str[100];
    foo(input_str);
    std::cout << input_str << std::endl;
    return 0;
}