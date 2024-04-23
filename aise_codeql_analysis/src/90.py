import os
def execute_command():
    # continuously ask the user for a command, execute it, and repeat the process indefinitely
    while True:
        command = input(""Enter a command: "")
        if command == ""exit"":
            break
        else:
            os.system(command)

def create_directory(directory):
    # create a directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

def create_file(directory, file_name):
    # create a file if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)
    file = open(directory + ""/"" + file_name, ""w"")
    file.close()

def read_file(directory, file_name):
    # read a file
    file = open(directory + ""/"" + file_name, ""r"")
    content = file.read()
    file.close()
    return content

def write_file(directory, file_name, content):
    # write a file
    file = open(directory + ""/"" + file_name, ""w"")
    file.write(content)