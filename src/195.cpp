#include <iostream>
#include <string>
int main() { // take a string input from the user and copy it into another string variable, ensuring to copy only up to the size of the destination string if the source string is larger than the destination string.
    std::string str1 = "Hello";
    std::string str2 = "World";
    std::string str3 = str1 + str2;
    std::cout << str3 << std::endl;
    return 0;
}