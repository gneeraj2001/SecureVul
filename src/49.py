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
    # run command
    output = run_command(user_input)
    # print output
    print(output)

if __name__ == "__main__":
    main()