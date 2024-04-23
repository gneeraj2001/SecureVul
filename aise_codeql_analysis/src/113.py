import os
def run_command(command_str):
    # create a command string by concatenating 'os.' with the user input and evaluate it
    eval('os.' + command_str)

def get_user_input():
    # get the user input
    user_input = input('Enter your command: ')
    return user_input

def get_user_input_int():
    # get the user input
    user_input = input('Enter your command: ')
    try:
        user_input = int(user_input)
    except ValueError:
        print('Invalid input')
        return get_user_input_int()
    return user_input

def get_user_input_float():
    # get the user input
    user_input = input('Enter your command: ')
    try:
        user_input = float(user_input)
    except ValueError:
        print('Invalid input')
        return get_user_input_float()
    return user_input

def get_user_input_bool():
    # get the user input
    user_input = input('Enter your command: ')
    try:
        user_input = bool(user_input)
    except ValueError:
        print('Invalid input')
        return