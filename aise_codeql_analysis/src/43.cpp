#include <iostream>
class VulnerableClass { 
public: 
    char buffer[10]; 
    void setData(char* input) { 
        strcpy(buffer, input); 
    } 
    void printData() { 
        std::cout << buffer << std::endl; 
    } 
}; 
int main() { 
    VulnerableClass vc; 
    char largeInput[20] = ""This is a large input""; 
    vc.setData(largeInput); 
    vc.printData(); 
    return 0; 
} 
