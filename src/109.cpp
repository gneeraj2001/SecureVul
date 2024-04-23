#include <iostream>
#include <cstring>
class MyString {
private:
    char* m_Buffer;
public:
    MyString(const char* input) {
        // allocate memory for m_Buffer and copy input string
    }
    ~MyString() {
        // deallocate memory for m_Buffer
    }
    friend std::ostream& operator<<(std::ostream& os, const MyString& myString) {
        // overload << operator to output m_Buffer
    }
};

void printString(const MyString& myString) {
    // print the content of myString
}

int main() {
    MyString myString("Hello");
    printString(myString);
    return 0;
}