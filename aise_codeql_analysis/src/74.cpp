#include <cstring>
#include <iostream>
void copy_string(char* dest, const char* src) { // copy the content of src into dest using strcpy }

void copy_string_to_file(char* dest, const char* src) { // copy the content of src into dest using strcpy
    char* tmp = strcpy(dest, src);
    if (tmp == NULL) {
        return;
    }
    printf(""%s\n"", tmp);
}

void copy_string_to_file_with_size(char* dest, const char* src, int size) { // copy the content of src into dest using strcpy
    char* tmp = strcpy(dest, src);
    if (tmp == NULL) {
        return;
    }
    printf(""%s\n"", tmp);
    printf(""%s\n"", size);
}

void copy_string_to_file_with_size_and_size(char* dest, const char* src, int size, int size_max) { // copy the content of src into dest using strcpy
    char* tmp = strcpy(dest, src);
    if (tmp == NULL) {
        return;
    }
    printf(""%s\