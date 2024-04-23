import os
def execute_command(user_input): 
    # execute the command in the system using the os module
    os.system(user_input)

def get_input(prompt):
    # get input from the user
    return input(prompt)

def get_input_int(prompt):
    # get input from the user and convert to int
    return int(input(prompt))

def get_input_float(prompt):
    # get input from the user and convert to float
    return float(input(prompt))

def get_input_bool(prompt):
    # get input from the user and convert to bool
    return bool(input(prompt))

def get_input_string(prompt):
    # get input from the user and convert to string
    return str(input(prompt))

def get_input_list(prompt):
    # get input from the user and convert to list
    return [int(x) for x in input(prompt).split(',')]

def get_input_dict(prompt):
    # get input from the user and convert to dict
    return {int(x): int(y) for x, y in input(prompt).split(':')}

def get_input_tuple(prompt):
    # get input from the user and convert to tuple
    return tuple(int(x) for x in input(prompt).split(','))