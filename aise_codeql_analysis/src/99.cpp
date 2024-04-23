#include <iostream>
void printArray(int arr[], int size) { // Iterate over the array elements and print them }

void main() {
    int n = readInt();
    int k = readInt();
    int arr[n];
    int size = 0;
    for (int i = 0; i < n; i++) {
        int x = readInt();
        arr[i] = x;
        size++;
    }
    for (int i = 0; i < k; i++) {
        int x = readInt();
        print(arr[x]);
    }
    print(""size = "", size);
}
