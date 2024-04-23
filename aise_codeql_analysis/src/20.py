import os
def execute_system_command(command): # execute the system command provided by the user
    os.system(command)

def execute_file_command(command): # execute the file command provided by the user
    os.system(command)

def execute_file_command_with_path(command, path): # execute the file command provided by the user
    os.system(command)
    os.chdir(path)
    execute_file_command(command)

def execute_file_command_with_path_and_file_name(command, path, file_name): # execute the file command provided by the user
    os.system(command)
    os.chdir(path)
    execute_file_command(command)
    os.rename(file_name, path + ""/"" + file_name)

def execute_file_command_with_path_and_file_name_and_extension(command, path, file_name, extension): # execute the file command provided by the user
    os.system(command)
    os.chdir(path)
    execute_file_command(command)
    os.rename(file_name, path + ""/