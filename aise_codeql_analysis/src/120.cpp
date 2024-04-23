#include <iostream>
class Buffer { 
public: 
    char buf[10]; 
    void setData(char data[]); 
    void printBuffer(); 
}; 

void Buffer::setData(char data[]) { 
    // copy the given character array into buf 
} 

void Buffer::printBuffer() { 
    // print out the content of buf 
} 

int main() { 
    Buffer bufferObj; 
    // use bufferObj to copy a large string into buf and then print it 
} 
