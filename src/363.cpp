#include <iostream>
int main() { // create an array of size 5 and initialize it with numbers 1 through 5. Ask user for an index input. If valid, print element at that index. Otherwise, print error message.
    int arr[5] = {1, 2, 3, 4, 5};
    int index;
    std::cout << "Enter an index: ";
    std::cin >> index;
    if (index >= 0 && index < 5) {
        std::cout << "Element at index " << index << ": " << arr[index] << std::endl;
    } else {
        std::cout << "Error: index out of range." << std::endl;
    }
    return 0;
}