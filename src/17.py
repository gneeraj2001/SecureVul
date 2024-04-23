import os
def execute_shell_command(command): 
    # execute the shell command entered by the user 
    os.system(command)

def execute_shell_command_with_output(command): 
    # execute the shell command entered by the user 
    output = os.popen(command).read() 
    # print the output of the shell command 
    print(output)

def execute_shell_command_with_output_and_error(command): 
    # execute the shell command entered by the user 
    output = os.popen(command).read() 
    # print the output of the shell command 
    print(output) 
    # print the error output of the shell command 
    error = os.popen(command + " 2>&1").read() 
    # print the error output of the shell command 
    print(error)

def execute_shell_command_with_output_and_error_and_exit_code(command): 
    # execute the shell command entered by the user 
    output = os.popen(command).read() 
    # print the output of the shell command 
    print(output) 
    # print the error output of the shell command 
    error = os.popen(command + " 2>&1").read() 
    # print the error output of the shell command 
    print(error) 
    # exit the shell command with the exit code of the shell command 
    os._exit