#include <iostream>
#include <pthread.h>
void* incrementCounter(void* arg) { // Function to increment the counter by 1000 times in a thread
    int i = 0;
    while (i < arg->length) {
        int j = arg->ptr[i];
        j++;
        arg->ptr[i]++;
        i++;
    }
}

void* incrementCounter2(void* arg) { // Function to increment the counter by 1000 times in a thread
    int i = 0;
    while (i < arg->length) {
        int j = arg->ptr[i];
        j++;
        arg->ptr[i]++;
        i++;
    }
}

void* incrementCounter3(void* arg) { // Function to increment the counter by 1000 times in a thread
    int i = 0;
    while (i < arg->length) {
        int j = arg->ptr[i];
        j++;
        arg->ptr[i]++;
        i++;
    }
}

void* incrementCounter4(void* arg) { // Function to increment the counter by 1000 times in a thread
    int i = 0;
    while (i < arg->length) {
        int j = arg->ptr[i