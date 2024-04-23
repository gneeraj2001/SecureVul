import os
def print_hello(user_input):
    # prints Hello, followed by user input
    os.system(f"echo Hello, {user_input}")

print_hello("World")