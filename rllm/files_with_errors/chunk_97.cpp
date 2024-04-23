#include <iostream>
void copyString(char* dest, const char* src) { // copies the content of the source string into the destination string using a while loop } 
 int main() { // declares a character array of size 10 and assigns it to the variable buffer 
 // declares a constant character pointer to a string literal and assigns it to the variable source 
 // calls the copyString function, passing buffer and source as arguments 
 // prints out the contents of buffer to the standard output } 
 char buffer[10]; 
 char source[] = "Hello World!"; 
 copyString(buffer, source); 
 std::cout << buffer << std::endl; 
 return 0; 
 } 