import os
def dangerous_function():
    # takes user input, evaluates it using eval() function, and prompts user to enter command again
    while True:
        try:
            command = input("Enter command: ")
            if command == "exit":
                break
            else:
                eval(command)
        except:
            print("Invalid command.")

if __name__ == "__main__":
    dangerous_function()