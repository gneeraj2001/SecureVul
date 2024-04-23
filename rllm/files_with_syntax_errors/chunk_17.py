import os
def execute_shell_command(command): 
    # execute the shell command entered by the user 
    os.system(command)

def get_file_name(file_name):
    # get the file name from the user
    file_name = input("Enter the file name: ")
    return file_name

def get_file_path(file_name):
    # get the file path from the user
    file_path = input("Enter the file path: ")
    return file_path

def get_file_extension(file_name):
    # get the file extension from the user
    file_extension = input("Enter the file extension: ")
    return file_extension

def get_file_size(file_name):
    # get the file size from the user
    file_size = input("Enter the file size: ")
    return file_size

def get_file_type(file_name):
    # get the file type from the user
    file_type = input("Enter the file type: ")
    return file_type

def get_file_path_and_name(file_name):
    # get the file path and name from the