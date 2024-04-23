import re
def function_name(input_string):
    # create a byte array of size 100 and store characters from input string
    byte_array = bytearray(100)
    for i in range(min(len(input_string), 100)):
        byte_array[i] = ord(input_string[i])
    return byte_array.decode('utf-8')

def main():
    # read input
    input_string = input()
    # convert to bytes
    input_string = input_string.encode('utf-8')
    # convert to function name
    function_name_string = function_name(input_string)
    # convert to function name
    function_name_string = function_name_string.replace(' ', '_')
    # convert to function name
    function_name_string = function_name_string.replace('(', '')
    function_name_string = function_name_string.replace(')', '')
    # convert to function name
    function_name_string = function_name_string.replace('"', '')
    # convert to function name
    function_name_string = function_name_string.replace('\'', '')