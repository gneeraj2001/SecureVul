#include <iostream>
#include <cstring>
void function1(char* input) { // copy the content of input to buffer using strcpy } int main() { // declare large_input array // initialize large_input with a string larger than buffer size // call function1 with large_input // return 0 }

void function2(char* input) { // copy the content of input to buffer using strcpy
    int i = 0;
    while (i < input.length()) {
        char c = input[i];
        if (c == '\n') {
            i++;
            break;
        }
        if (c == '\r') {
            i++;
            break;
        }
        if (c == '\t') {
            i++;
            break;
        }
        if (c =='') {
            i++;
            break;
        }
        if (c == '\b') {
            i++;
            break;
        }
        if (c == '\f') {
            i++;
            break;
        }
        if (c == '\f') {
            i++;
            break;
        }
        if (c == '\f') {
            i++;
            break;
        }
        if (c == '\f') {
            i++;
            break;
        }
        if (c == '\f