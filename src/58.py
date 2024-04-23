import os
def run_command():
    # takes user input, evaluates it into a command, and executes the command
    command = input("Enter a command:")
    os.system(command)

def main():
    # runs the command loop
    while True:
        run_command()

if __name__ == "__main__":
    main()