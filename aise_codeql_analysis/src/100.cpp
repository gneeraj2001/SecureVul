#include <iostream>
#include <string.h>
void copyString(char* dest, const char* src) { // use the strcpy function to copy the content of src into dest }

void copyString(const char* dest, const char* src) { // use the strcpy function to copy the content of src into dest }

void copyString(const char* dest, const char* src, int n) { // use the strcpy function to copy the content of src into dest and n times
	int i = 0;
	while (i < n) {
		dest = strcpy(dest, src, i);
		i++;
	}
}

void copyString(const char* dest, const char* src, int n) { // use the strcpy function to copy the content of src into dest and n times
	int i = 0;
	while (i < n) {
		dest = strcpy(dest, src, i);
		i++;
	}
}

void copyString(const char* dest, const char* src, int n) { // use the strcpy function to copy the content of src into dest and n times
	int i = 0;
	while (i < n) {
		dest = strcpy(dest, src, i);
