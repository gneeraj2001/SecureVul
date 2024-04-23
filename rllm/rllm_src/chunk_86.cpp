#include <iostream>
#include <cstring>
void vulnerableFunction(char* input) { // Declare a character array buffer of size 10. Copy the content of the input character array into the buffer using strcpy. Print out the content of the buffer using cout.
    char buffer[10];
    strcpy(buffer, input);
    std::cout << buffer << std::endl;
}
int main() {
    char input[10];
    std::cout << "Enter a string: ";
    std::cin >> input;
    vulnerableFunction(input);
    return 0;
}