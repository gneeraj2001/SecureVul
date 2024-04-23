#include <iostream>
int main() { // print the maximum value of an integer and cause an overflow by adding 1 to it
    int a = 1000000000;
    int b = 1000000000;
    std::cout << "The maximum value of a is " << a << std::endl;
    std::cout << "The maximum value of b is " << b << std::endl;
    a += 1;
    b += 1;
    std::cout << "The maximum value of a is " << a << std::endl;
    std::cout << "The maximum value of b is " << b << std::endl;
    return 0;
}