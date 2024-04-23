import os
def execute_user_command():
    # prompt user to enter a command and execute it using os.system
    # if the command is invalid, the user will be prompted to enter a valid command
    # if the command is valid, the user will be prompted to enter a new command
    # if the user enters 'exit', the program will exit
    while True:
        command = input("Enter a command: ")
        if command == "exit":
            break
        elif command == "help":
            print("Available commands: ")
            print("exit - exits the program")
            print("help - prints this help message")
            print("add - adds a new user to the database")
            print("remove - removes a user from the database")
            print("list - lists all users in the database")
            print("update - updates a user's information in the database")
            print("exit - exits the program")
        else:
            try:
                os.system(command)
            except:
                print("Invalid command")

execute_user_command()