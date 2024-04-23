#include <iostream>
#include <cstring>
void copyString(char* dest, const char* src) { // Copy the content of src into dest using strcpy function }
void copyString(const char* dest, const char* src) { // Copy the content of src into dest using strcpy function }
void copyString(const char* dest, const char* src, int n) { // Copy the content of src into dest using strcpy function and n
    int i = 0;
    while (i < n) {
        dest = strcpy(dest, src, i);
        i++;
    }
}
void copyString(const char* dest, const char* src, int n) { // Copy the content of src into dest using strcpy function and n
    int i = 0;
    while (i < n) {
        dest = strcpy(dest, src, i);
        i++;
    }
}
void copyString(const char* dest, const char* src, int n) { // Copy the content of src into dest using strcpy function and n
    int i = 0;
    while (i < n) {
        dest = strcpy(dest, src, i);
        i++;
    }
}
void copyString(const char