import os
def execute_system_command(user_input): 
    # execute system command with user input using the os module
    os.system(user_input)

def execute_system_command_with_output(user_input):
    # execute system command with user input using the os module
    os.system(user_input)
    # get the output of the command
    output = os.popen(user_input).read()
    return output

def execute_system_command_with_output_and_error(user_input):
    # execute system command with user input using the os module
    os.system(user_input)
    # get the output of the command
    output = os.popen(user_input).read()
    # get the error of the command
    error = os.popen(user_input + " 2>&1").read()
    return output, error

def execute_system_command_with_output_and_error_and_exit_code(user_input):
    # execute system command with user input using the os module
    os.system(user_input)
    # get the output of the command
    output = os.popen(user_input).read()
    # get the error of the command
    error = os.popen(user_input + " 2>&1").read()
    # get the exit code of