import os
def evaluate_string(input_string):
    return eval(input_string)

def evaluate_file(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
    return evaluate_string(lines[0])

def evaluate_file_list(input_file_list):
    return [evaluate_file(f) for f in input_file_list]

def evaluate_file_list_with_path(input_file_list):
    return [evaluate_file(f) for f in input_file_list]

def evaluate_file_list_with_path_and_name(input_file_list):
    return [evaluate_file(f) for f in input_file_list]

def evaluate_file_list_with_path_and_name_and_extension(input_file_list):
    return [evaluate_file(f) for f in input_file_list]

def evaluate_file_list_with_path_and_name_and_extension_and_extension(input_file_list):
    return [evaluate_file(f) for f in input_file