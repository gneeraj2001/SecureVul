#include <iostream>
#include <cstring>
void copyString(char* input)
{
    std::cout << "Enter the string: ";
    std::cin >> input;
}

int main()
{
    char input[100];
    copyString(input);
    std::cout << input << std::endl;
    return 0;
}