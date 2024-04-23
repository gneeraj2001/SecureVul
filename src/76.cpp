#include <iostream>
#include <cstring>
void concatenateStrings(char str1[], char str2[]) { // Concatenate two strings and print the result
    int len1 = strlen(str1);
    int len2 = strlen(str2);
    char *result = new char[len1 + len2 + 1];
    strcpy(result, str1);
    strcat(result, str2);
    std::cout << result << std::endl;
}

int main() {
    char str1[] = "Hello";
    char str2[] = "World";
    concatenateStrings(str1, str2);
    return 0;
}