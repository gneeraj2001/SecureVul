#include <iostream>
#include <string>
int main() { // take a string input from the user and copy it into another string variable, truncating if necessary
    std::string str = "Hello World";
    std::string str2 = str.substr(0, 5); // take the first 5 characters of the string str and copy them into str2
    std::cout << str2 << std::endl; // print the result
    return 0;
}