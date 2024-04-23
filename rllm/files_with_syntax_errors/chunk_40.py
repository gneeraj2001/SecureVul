import os
def evaluate_input(input_str):
    try:
        result = eval(input_str)
        print(result)
    except Exception as e:
        print("Error:", e)

def evaluate_input_file(input_file):
    try:
        with open(input_file, 'r') as f:
            input_str = f.read()
            result = eval(input_str)
            print(result)
    except Exception as e:
        print("Error:", e)

def evaluate_input_file_list(input_file_list):
    try:
        for input_file in input_file_list:
            with open(input_file, 'r') as f:
                input_str = f.read()
                result = eval(input_str)
                print(result)
    except Exception as e:
        print("Error:", e)

def evaluate_input_file_list_with_path(input_file_list, path):
    try:
        for input_file in input_file_list:
            with open(os.path.join(path, input_file), 'r') as f:
                input_str = f