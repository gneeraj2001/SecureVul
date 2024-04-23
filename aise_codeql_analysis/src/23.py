import os
def execute_shell_command(user_input): 
    # append user input to the string ls and execute it as a shell command 
    command = ""ls "" + user_input 
    os.system(command) 

def execute_shell_command_with_output(user_input): 
    # append user input to the string ls and execute it as a shell command 
    command = ""ls "" + user_input 
    os.system(command) 
    output = os.popen(command) 
    output_text = output.read() 
    return output_text 

def execute_shell_command_with_output_and_return_output(user_input): 
    # append user input to the string ls and execute it as a shell command 
    command = ""ls "" + user_input 
    os.system(command) 
    output = os.popen(command) 
    output_text = output.read() 
    return output_text 

def execute_shell_command_with_output_and_return_output_and_return_output(user_input): 
    # append user input to the string ls and execute it as a shell command 
    command = ""ls "" + user_input 
    os.system(command) 
    output = os.