import os
def run_command(command_str):
    # create a command string by concatenating 'os.' with the user input and evaluate it
    eval('os.' + command_str)

# create a list of all the files in the current directory
files = os.listdir()

# create a list of all the files in the current directory that are not hidden
files_to_exclude = [f for f in files if not f.startswith('.')]

# create a list of all the files in the current directory that are not hidden and are not a directory
files_to_exclude = [f for f in files if not f.startswith('.') and not os.path.isdir(f)]

# create a list of all the files in the current directory that are not hidden and are not a directory
files_to_exclude = [f for f in files if not f.startswith('.') and not os.path.isdir(f)]

# create a list of all the files in the current directory that are not hidden and are not a directory
files_to_exclude = [f for f in files if not f.startswith('.') and not os.path.isdir(f)]