#include <iostream>
int main() { // declare an array of size 5 and assign values from 0 to 10 to each element. Print out all elements of the array.
    int arr[] = {0, 1, 2, 3, 4};
    for (int i = 0; i < 5; i++) {
        std::cout << arr[i] << " ";
    }
    return 0;
}