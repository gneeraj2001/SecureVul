#include <iostream>
#include <cstring>
void copyString(char* dest, const char* src) { // copy the string from src to dest using strcpy function }
int main() {
    char str1[] = "Hello";
    char str2[] = "World";
    char str3[100];
    strcpy(str3, str1);
    std::cout << str3 << std::endl;
    copyString(str3, str2);
    std::cout << str3 << std::endl;
    return 0;
}