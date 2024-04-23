import os
def evaluate_input(user_input):
    return eval(user_input)

while True:
    user_code = input("Enter some Python code:")
    evaluate_input(user_code)