import os
def run_command(user_input):
    # construct command by concatenating "ls -l " with user input
    # execute the command in the system shell
    # return the output of the command
    command = "ls -l " + user_input
    output = os.popen(command).read()
    return output

def main():
    # get user input
    user_input = input("Enter a file name: ")
    # run the command
    output = run_command(user_input)
    # print the output
    print(output)

if __name__ == "__main__":
    main()