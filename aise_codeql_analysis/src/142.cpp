#include <iostream>
#include <string.h>
void copyString(char* dest, const char* src) { // use strcpy to copy src to dest }

void copyString(const char* dest, const char* src) { // use strcpy to copy dest to src
    char* tmp = dest;
    char* tmp2 = src;
    while (tmp!= tmp2) {
        if (tmp == tmp2) {
            printf(""%s\n"", tmp);
            break;
        }
        tmp = tmp2;
        tmp2 = tmp2 + 1;
    }
}

void copyString(const char* dest, const char* src) { // use strcpy to copy dest to src
    char* tmp = dest;
    char* tmp2 = src;
    while (tmp!= tmp2) {
        if (tmp == tmp2) {
            printf(""%s\n"", tmp);
            break;
        }
        tmp = tmp2;
        tmp2 = tmp2 + 1;
    }
}

void copyString(const char* dest, const char* src) { // use strcpy to copy dest to src
    char* tmp = dest;
    char* tmp2 = src;
    while (