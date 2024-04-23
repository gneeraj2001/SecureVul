#include <iostream>
int main() { // create an array of 5 integers and ask user for an index to print the integer at that index
    int arr[] = {1, 2, 3, 4, 5};
    int index;
    std::cout << "Enter an index: ";
    std::cin >> index;
    std::cout << "The integer at index " << index << " is " << arr[index] << std::endl;
    return 0;
}