#include <iostream>
#include <cstring>
void unsafe_function(char* input) { // Declare a character array buffer of size 10. Copy the contents of the input character array into the buffer using strcpy. Print out the content of the buffer. }
int main() {
    char input[10];
    std::cout << "Enter a string: ";
    std::cin >> input;
    unsafe_function(input);
    std::cout << "The contents of the buffer are: " << input << std::endl;
    return 0;
}