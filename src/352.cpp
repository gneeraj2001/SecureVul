#include <iostream>
#include <cstring>
void vulnerableFunction(char* input) { // create a character array of size 10 and copy the content of the input character pointer into this array
    char* buffer = new char[10];
    strcpy(buffer, input);
    std::cout << buffer << std::endl;
    delete[] buffer;
}

int main() {
    char input[] = "Hello World";
    vulnerableFunction(input);
    return 0;
}