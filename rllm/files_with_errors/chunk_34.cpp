#include <iostream>
#include <string.h>
void func(char* input_str) { // Declare a character array buffer of size 10. Copy the content of input string into buffer using strcpy(). Print out the copied string. }
int main() {
    char input_str[10];
    strcpy(input_str, "Hello");
    func(input_str);
    return 0;
}