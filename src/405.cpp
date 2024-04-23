#include <iostream>
void function1() { // allocate memory for a character array of size 10 and read user input into the buffer using std::cin. After reading, deallocate the memory allocated for the buffer.
    char buffer[10];
    std::cin >> buffer;
    std::cout << buffer << std::endl;
}

int main() {
    function1();
    return 0;
}