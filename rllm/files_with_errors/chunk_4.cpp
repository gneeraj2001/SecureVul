#include <iostream>
#include <cstring>
void func(char* input_str) { // Copy the content of the input string into a buffer using strcpy and print the buffer using cout
    char* buffer = new char[strlen(input_str) + 1];
    strcpy(buffer, input_str);
    cout << buffer << endl;
    delete[] buffer;
}
int main() {
    char input_str[] = "Hello World!";
    func(input_str);
    return 0;
}
