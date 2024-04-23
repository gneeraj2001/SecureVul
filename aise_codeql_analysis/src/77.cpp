#include <iostream>
#include <cstring>
void copyString(char* dest, const char* src) { // copy the content of src into dest using strcpy function } int main() { // declare buffer array of size 10 // declare constant character pointer source initialized with a long string // call copyString function, passing buffer and source as arguments // print out the content of buffer using std::cout // return 0 }

int main() {
    char * buffer = (char *) malloc(10);
    printf(""Hello, World!\n"");
    copyString(buffer, ""Hello, World!"");
    return 0;
}
