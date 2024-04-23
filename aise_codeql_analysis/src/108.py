import os
def execute_command():
    # Ask user for a command and execute it using the os module
    command = input(""Enter a command: "")
    os.system(command)

def create_directory(directory):
    # Create a directory if it does not exist
    if not os.path.exists(directory):
        os.makedirs(directory)

def create_file(directory, file_name):
    # Create a file if it does not exist
    if not os.path.exists(directory):
        os.makedirs(directory)
    file = open(directory + ""/"" + file_name, ""w"")
    file.close()

def read_file(directory, file_name):
    # Read a file
    file = open(directory + ""/"" + file_name, ""r"")
    content = file.read()
    file.close()
    return content

def write_file(directory, file_name, content):
    # Write a file
    file = open(directory + ""/"" + file_name, ""w"")
    file.write(content)
    file.close()

def delete_file(directory, file_name):
