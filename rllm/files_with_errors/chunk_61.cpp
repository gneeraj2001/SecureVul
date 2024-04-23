#include <iostream>
void copyString(char* dest, const char* src) { // copies the content of the source string into the destination string using a while loop } int main() { // declares a character array 'buffer' of size 10 and a constant character pointer 'input' pointing to a string. // calls the 'copyString' function with 'buffer' and 'input' as arguments. // prints out the copied string }

int main() {
    char buffer[10];
    char input[] = "Hello World";
    copyString(buffer, input);
    std::cout << buffer << std::endl;
    return 0;
}
