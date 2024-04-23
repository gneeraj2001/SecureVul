import threading
def increment_counter(counter): 
    for _ in range(100000): 
        counter += 1 

def decrement_counter(counter): 
    for _ in range(100000): 
        counter -= 1 

def increment_counter_thread(counter): 
    for _ in range(100000): 
        counter += 1 

def decrement_counter_thread(counter): 
    for _ in range(100000): 
        counter -= 1 

def increment_counter_thread_2(counter): 
    for _ in range(100000): 
        counter += 1 

def decrement_counter_thread_2(counter): 
    for _ in range(100000): 
        counter -= 1 

def increment_counter_thread_3(counter): 
    for _ in range(100000): 
        counter += 1 

def decrement_counter_thread_3(counter): 
    for _ in range(100000): 
        counter -= 1 

def increment_counter_thread_4(counter): 
    for _ in range(100000): 
        counter += 1 

def decrement_counter_thread_4(counter): 
    for _ in range(100000): 
        counter -= 1