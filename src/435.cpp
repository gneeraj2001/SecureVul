#include <iostream>
#include <cstring>
class VulnerableClass {
public:
    char* buffer;
    int bufferSize;

    VulnerableClass(int size) {
        bufferSize = size;
        buffer = new char[bufferSize];
    }

    ~VulnerableClass() {
        delete[] buffer;
    }

    void setData(const char* data) {
        strncpy(buffer, data, bufferSize);
    }

    void printBuffer() {
        std::cout << buffer << std::endl;
    }
};

int main() {
    VulnerableClass v(10);
    v.setData("Hello World!");
    v.printBuffer();
    return 0;
}