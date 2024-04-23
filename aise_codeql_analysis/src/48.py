import subprocess
def execute_command(command): 
    # execute a command in the terminal using subprocess module
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output, error

def get_output(command):
    # get the output of the command using subprocess module
    output, error = execute_command(command)
    return output

def get_error(command):
    # get the error of the command using subprocess module
    output, error = execute_command(command)
    return error

def get_output_as_string(command):
    # get the output of the command using subprocess module
    output = get_output(command)
    return output

def get_error_as_string(command):
    # get the error of the command using subprocess module
    output = get_error(command)
    return output

def get_output_as_list(command):
    # get the output of the command using subprocess module
    output = get_output(command)
    return output

def get_error