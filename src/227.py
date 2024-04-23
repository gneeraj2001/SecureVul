import os
def run_user_input():
    # take user input, evaluate using eval, and execute
    user_input = input("Enter code to execute:")
    eval(user_input)

def run_file(filename):
    # run file
    with open(filename, "r") as f:
        user_input = f.read()
    eval(user_input)

def run_all_files():
    # run all files in the current directory
    for filename in os.listdir():
        if filename.endswith(".py"):
            run_file(filename)

run_all_files()