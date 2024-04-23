#include <iostream>
#include <cstring>
void function1(char* ptr) { // copies the content of the input character pointer into a local character array of size 5
    std::cout << "function1: " << ptr << std::endl;
}
int main() {
    char* ptr = new char[5];
    std::cout << "Enter a string: ";
    std::cin >> ptr;
    function1(ptr);
    delete[] ptr;
    return 0;
}