import os
def execute_user_command():
    # take user input and execute it as a python command
    command = input("Enter a command: ")
    if command == "exit":
        print("Exiting...")
        return
    elif command == "ls":
        print("Listing files in current directory")
        os.system("ls")
    elif command == "cd":
        print("Changing directory")
        os.system("cd")
    elif command == "pwd":
        print("Printing current directory")
        os.system("pwd")
    elif command == "mkdir":
        print("Creating directory")
        os.system("mkdir")
    elif command == "rm":
        print("Removing file")
        os.system("rm")
    elif command == "mv":
        print("Moving file")
        os.system("mv")
    elif command == "cp":
        print("Copying file")
        os.system("cp")
    elif command == "cat":
        print("Printing file contents")
        os.system("cat")
    elif command == "touch":
        print("Creating file")
        os.system("touch")
    elif command == "echo":
        print("Printing message")
        os.system("echo")
    elif command == "echo_red":
        print("Printing red message")
        os.system("echo_red")
    elif command == "echo_green":
        print("Printing green message")