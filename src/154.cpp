#include <iostream>
#include <cstring>
int main() { // read an integer from user input and pass it to a function to copy a string into a character array and print the character at the specified index
    char a[10];
    int n;
    std::cout << "Enter a number: ";
    std::cin >> n;
    std::cout << "Enter a string: ";
    std::cin >> a;
    std::cout << "The character at index " << n << " is: " << a[n];
    return 0;
}