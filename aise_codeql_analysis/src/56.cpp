import os
def run_command(user_input):
    # construct command by concatenating ""ls -l "" with user input
    # execute the command in the system shell
    # return the output of the command
    command = ""ls -l "" + user_input
    print(command)
    os.system(command)

def run_command_with_output(user_input):
    # construct command by concatenating ""ls -l "" with user input
    # execute the command in the system shell
    # return the output of the command
    command = ""ls -l "" + user_input
    print(command)
    os.system(command)
    output = os.popen(command).read()
    return output

def run_command_with_output_and_return_output(user_input):
    # construct command by concatenating ""ls -l "" with user input
    # execute the command in the system shell
    # return the output of the command
    command = ""ls -l "" + user_input
    print(command)
    os.system(command)
    output = os.popen(command).read()
    return output

def run_command_with_output_and_return_output_and_return_output(user