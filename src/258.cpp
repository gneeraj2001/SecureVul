#include <iostream>
#include <cstring>
int main() { 
    char buffer[10];
    char source[] = "This is a long string that will cause a buffer overflow!";
    strcpy(buffer, source);
    std::cout << buffer << std::endl;
}