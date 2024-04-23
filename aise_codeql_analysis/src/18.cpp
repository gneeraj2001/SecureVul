#include <iostream>
#include <cstring>
void copy_input(char* dest, int size) { // read input from standard input into the dest character array }
void copy_output(char* dest, int size) { // copy the output to the dest character array }
void copy_output_to_file(char* dest, int size) { // copy the output to the dest file
    int i = 0;
    while (i < size) {
        char c = stdin.read(1);
        dest[i] = c;
        i++;
    }
}
void copy_output_to_file_to_file(char* dest, int size) { // copy the output to the dest file
    int i = 0;
    while (i < size) {
        char c = stdout.read(1);
        dest[i] = c;
        i++;
    }
}
void copy_input_to_file(char* dest, int size) { // copy the input to the dest file
    int i = 0;
    while (i < size) {
        char c = stdin.read(1);
        dest[i] = c;
        i++;
    }
}
void copy_output_to_file_to_