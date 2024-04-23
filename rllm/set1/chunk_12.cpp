#include <iostream>
#include <pthread.h>
void* incrementCounter(void* arg) { // Function to increment the counter by 1000 times in a thread
    int* counter = (int*)arg;
    for (int i = 0; i < 1000; i++) {
        (*counter)++;
    }
    return NULL;
}
int main() {
    int counter = 0;
    pthread_t thread1, thread2;
    pthread_create(&thread1, NULL, incrementCounter, &counter);
    pthread_create(&thread2, NULL, incrementCounter, &counter);
    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);
    std::cout << counter << std::endl;
    return 0;
}