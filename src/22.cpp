#include <iostream>
#include <cstring>
void func(char* input_str) { // Copy the content of the input string into a buffer and print it using cout
    char buffer[100];
    strcpy(buffer, input_str);
    std::cout << buffer << std::endl;
}
int main() {
    char input_str[] = "Hello World!";
    func(input_str);
    return 0;
}