#include <iostream>
void printArray(int arr[], int size) { // Iterate over the array elements and print them }
int main() {
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int size = sizeof(arr) / sizeof(int);
    printArray(arr, size);
    return 0;
}