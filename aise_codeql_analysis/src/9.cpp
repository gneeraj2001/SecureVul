#include <iostream>
#include <cstring>
void unsafe_function(char* input) { // Declare a character array buffer of size 10. Copy the contents of the input character array into the buffer using strcpy. Print out the content of the buffer. }
void unsafe_function(char* input) {
    char *buffer = (char *) malloc(10);
    printf(""%c"", input);
    memcpy(buffer, input, sizeof(input));
    return 0;
}
void unsafe_function(char* input) {
    char *buffer = (char *) malloc(10);
    printf(""%c"", input);
    memcpy(buffer, input, sizeof(input));
    return 0;
}
void unsafe_function(char* input) {
    char *buffer = (char *) malloc(10);
    printf(""%c"", input);
    memcpy(buffer, input, sizeof(input));
    return 0;
}
void unsafe_function(char* input) {
    char *buffer = (char *) malloc(10);
    printf(""%c"", input);
    memcpy(buffer, input, sizeof(input));
    return 0;
}
void unsafe_function(char* input) {
    char *buffer = (char *) malloc(10);
    printf(""%c"", input);
    