#include <iostream>
#include <cstring>
void copyString(char* dest, const char* src) { // use the strcpy function to copy the content of src into dest }

void copyString(const char* dest, const char* src) { // use the strcpy function to copy the content of src into dest }

void copyString(const char* dest, const char* src, int n) { // use the strcpy function to copy the content of src into dest and n times
	int i = 0;
	while (i < n) {
		char c = src[i];
		dest[i] = c;
		i++;
	}
}

void copyString(const char* dest, const char* src, int n) { // use the strcpy function to copy the content of src into dest and n times
	int i = 0;
	while (i < n) {
		char c = src[i];
		dest[i] = c;
		i++;
	}
}

void copyString(const char* dest, const char* src, int n) { // use the strcpy function to copy the content of src into dest and n times
	int i = 0;
	while (i < n) {
		char c = src[