#include <iostream>
#include <cstring>
void vulnerable_function(char* input) { // Declare a character array buffer of size 10 and copy the input string into it using strcpy. Print the contents of the buffer using cout.
    cout << input << endl;
    return 0;
}

void main() {
    char *input = """";
    while (input!= """") {
        char *output = vulnerable_function(input);
        cout << output << endl;
        input = input + """";
    }
}

void main() {
    char *input = """";
    while (input!= """") {
        char *output = vulnerable_function(input);
        cout << output << endl;
        input = input + """";
    }
}

void main() {
    char *input = """";
    while (input!= """") {
        char *output = vulnerable_function(input);
        cout << output << endl;
        input = input + """";
    }
}

void main() {
    char *input = """";
    while (input!= """") {
        char *output = vulnerable_function(input);
        cout << output << endl;
        input = input + """";
    }
}

void main() {
