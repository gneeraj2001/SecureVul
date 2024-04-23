import os
def execute_system_command(command): 
    # execute the system command provided by the user 
    os.system(command) 

def execute_file_command(command): 
    # execute the file command provided by the user 
    os.system(command) 

def execute_file_command_with_path(command, path): 
    # execute the file command provided by the user 
    os.system(command) 
    os.chdir(path) 
    os.system(command) 

def execute_file_command_with_path_and_name(command, path, name): 
    # execute the file command provided by the user 
    os.system(command) 
    os.chdir(path) 
    os.system(command) 
    os.rename(name, name) 

def execute_file_command_with_path_and_name_and_name(command, path, name, name2): 
    # execute the file command provided by the user 
    os.system(command) 
    os.chdir(path) 
    os.system(command) 
    os.rename(name, name) 
    os.ren