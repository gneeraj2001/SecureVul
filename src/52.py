import re
def function_name(input_string):
    # create a byte array of size 100 and store characters from input string
    byte_array = bytearray(100)
    for i in range(min(len(input_string), 100)):
        byte_array[i] = ord(input_string[i])
    return byte_array.decode('utf-8')

def get_function_name(input_string):
    # create a byte array of size 100 and store characters from input string
    byte_array = bytearray(100)
    for i in range(min(len(input_string), 100)):
        byte_array[i] = ord(input_string[i])
    return byte_array.decode('utf-8')

def get_function_name_from_file(filename):
    # open file
    with open(filename, 'r') as f:
        # read file
        input_string = f.read()
        # get function name
        function_name = get_function_name(input_string)
        return function_name

def get_function_name_from_file_and_replace(filename, replace_string):
    # open file
    with open(filename, 'r') as f:
        # read file
        input_string = f.read()