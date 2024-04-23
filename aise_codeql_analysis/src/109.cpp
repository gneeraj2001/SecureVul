#include <iostream>
#include <cstring>
void copyString(char* dest, const char* src) { // copy the content of src into dest using strcpy function } int main() { // declare a character array buffer of size 10 // initialize buffer with a string input that is too long to fit // call copyString function with buffer and input as arguments // print the contents of buffer }

int main() {
    char *buffer = (char *) malloc(10);
    printf(""Hello, World!\n"");
    copyString(buffer, ""Hello, World!"");
    printf(""\n"");
    return 0;
}
