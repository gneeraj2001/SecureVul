import re
def dangerous_function(user_input):
    # execute the user_input as python code
    exec(user_input)

def main():
    # get the input from the user
    user_input = input("Enter a python code: ")
    # execute the user_input as python code
    dangerous_function(user_input)

if __name__ == "__main__":
    main()