#include <iostream>
#include <cstring>
void func(char* input_str) { // Copy the content of the input string into a buffer and print it using cout
    std::cout << input_str << std::endl;
}
int main() {
    char input_str[100];
    std::cout << "Enter a string: ";
    std::cin >> input_str;
    func(input_str);
    return 0;
}