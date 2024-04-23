import os
def execute_command():
    # Ask user for a command and execute it using the os module
    command = input("Enter a command: ")
    os.system(command)

execute_command()