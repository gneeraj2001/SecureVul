#include <iostream>
#include <cstring>
void vulnerable_function(char* input) { // Declare a character array buffer of size 10 and copy the input string into it using strcpy. Print the contents of the buffer using cout.
  char buffer[10];
  strcpy(buffer, input);
  std::cout << buffer << std::endl;
}

int main() {
  char input[] = "Hello World!";
  vulnerable_function(input);
  return 0;
}