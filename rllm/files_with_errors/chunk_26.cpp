#include <iostream>
#include <string>
void copyString(string source, string &destination) { // copy the content of the source string into the destination string }
int main() {
    string source = "Hello";
    string destination;
    copyString(source, destination);
    cout << destination << endl;
    return 0;
}