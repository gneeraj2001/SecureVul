#include <iostream>
#include <cstring>
using namespace std;
class VulnerableClass { 
public: 
    char buffer[10]; 
    void setData(char* input) { 
        strcpy(buffer, input); 
    } 
    void printBuffer() { 
        cout << buffer << endl; 
    } 
}; 

int main() { 
    VulnerableClass vc; 
    char largeInput[20] = ""This is a large input""; 
    vc.setData(largeInput); 
    vc.printBuffer(); 
    return 0; 
} 
