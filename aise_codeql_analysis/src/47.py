import subprocess
def execute_command(user_input):
    # execute the command using subprocess.Popen
    command = user_input
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output, error

def get_output(command):
    # get the output of the command using subprocess.Popen
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output, error

def get_output_error(command):
    # get the output of the command using subprocess.Popen
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output, error

def get_output_error_by_command(command):
    # get the output of the command using subprocess.Popen
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output, error

def get_output_error_by_command_and