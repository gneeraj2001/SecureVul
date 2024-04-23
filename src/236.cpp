#include <iostream>
int main() { // declare a character array of size 10, fill it with character 'A' from index 0 to 15, add a null character at index 16, and print the contents of the buffer.
    char buffer[10] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', '\0'};
    std::cout << buffer << '\n'; // prints 'ABCDE'
    buffer[16] = 'X'; // add a character at index 16
    std::cout << buffer << '\n'; // prints 'ABCDEX'
    return 0;
}