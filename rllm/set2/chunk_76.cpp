#include <iostream>
#include <cstring>
void concatenateStrings(char str1[], char str2[]) { // Concatenate two strings and print the result
    int i = 0;
    int j = 0;
    int k = 0;
    while (str1[i]!= '\0') {
        str1[k] = str1[i];
        k++;
        i++;
    }
    while (str2[j]!= '\0') {
        str1[k] = str2[j];
        k++;
        j++;
    }
    str1[k] = '\0';
}
int main() {
    char str1[100];
    char str2[100];
    std::cout << "Enter the first string: ";
    std::cin >> str1;
    std::cout << "Enter the second string: ";
    std::cin >> str2;
    concatenateStrings(str1, str2);
    std::cout << "The concatenated string is: " << str1 << std::endl;
    return 0;
}