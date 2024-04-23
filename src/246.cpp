#include <iostream>
#include <cstring>
void copyString(char* str1, char* str2) { 
    // copy the content of one string into another using strcpy function
    strcpy(str1, str2); 
}
int main() {
    char str1[100], str2[100];
    copyString(str1, str2);
    std::cout << str1 << std::endl;
    std::cout << str2 << std::endl;
    return 0;
}