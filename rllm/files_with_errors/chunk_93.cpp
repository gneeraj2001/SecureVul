#include <iostream>
class MemoryLeakClass { // constructor allocates an array of 100 integers, destructor does not deallocate memory } int main() { // create an instance of MemoryLeakClass in a loop 1 million times and immediately delete it }
