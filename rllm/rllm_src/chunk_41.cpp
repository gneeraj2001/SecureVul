#include <iostream>
#include <string>
#include <cstring>
class VulnerableClass { public: VulnerableClass(int size) : bufferSize(size) { buffer = new char[bufferSize]; } ~VulnerableClass() { delete[] buffer; } void setData(std::string data) { strncpy(buffer, data.c_str(), bufferSize); } void printBuffer() { std::cout << buffer << std::endl; } private: char* buffer; int bufferSize; };
int main() {
  VulnerableClass v(10);
  v.setData("Hello World");
  v.printBuffer();
  return 0;
}