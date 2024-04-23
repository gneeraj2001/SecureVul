import os
def unsafe_function(user_input):
    # execute user input using eval
    eval(user_input)

def main():
    # get the input from the user
    user_input = input("Enter your input: ")
    # execute the input
    unsafe_function(user_input)

if __name__ == "__main__":
    main()