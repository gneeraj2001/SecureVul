import os
import sys
def run_command(user_input):
    # Execute user_input as Python code using eval
    eval(user_input)

def main():
    # Ask for a command
    user_input = input("Enter a command: ").strip()
    # Call run_command function with user_input
    run_command(user_input)

if __name__ == "__main__":
    main()