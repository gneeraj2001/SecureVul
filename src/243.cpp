#include <iostream>
#include <cstring>
void func(char* input) { // Copy the content of the input character pointer into the buffer using the strcpy function.
    char* buffer = new char[strlen(input) + 1];
    strcpy(buffer, input);
    std::cout << buffer << std::endl;
}
int main() {
    char input[] = "Hello";
    func(input);
    return 0;
}