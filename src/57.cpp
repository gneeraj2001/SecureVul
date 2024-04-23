#include <iostream>
int main() { // create an array of 5 integers with numbers from 1 to 5 and print them using a for loop
    int arr[5] = {1, 2, 3, 4, 5};
    for (int i = 0; i < 5; i++) {
        std::cout << arr[i] << " ";
    }
    return 0;
}