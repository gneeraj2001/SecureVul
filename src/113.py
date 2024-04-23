import re
def evaluate_input():
    # prompt user to enter Python code, store in user_input, and execute using eval()
    user_input = input("Enter Python code: ")
    user_input = user_input.strip()
    eval(user_input)

def evaluate_input_with_prompt():
    # prompt user to enter Python code, store in user_input, and execute using eval()
    user_input = input("Enter Python code: ")
    user_input = user_input.strip()
    eval(user_input)
    print("Your code has been evaluated and stored in user_input.")

def evaluate_input_with_prompt_and_store_in_variable():
    # prompt user to enter Python code, store in user_input, and execute using eval()
    user_input = input("Enter Python code: ")
    user_input = user_input.strip()
    eval(user_input)
    print("Your code has been evaluated and stored in user_input.")
    user_input = user_input

def evaluate_input_with_prompt_and_store_in_variable_and_print():
    # prompt user to enter Python code, store in user_input, and execute using eval()
    user_input = input("Enter Python code: ")
    user_input = user_input.strip()
    eval(user_input)