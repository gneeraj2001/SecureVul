import os
def execute_command(user_input): 
    # execute the command in the system using the os module
    os.system(user_input)

def execute_command_with_output(user_input, output_file):
    # execute the command in the system using the os module
    os.system(user_input)
    with open(output_file, 'w') as f:
        f.write(output_file)

def execute_command_with_output_and_print(user_input, output_file, print_output):
    # execute the command in the system using the os module
    os.system(user_input)
    with open(output_file, 'w') as f:
        f.write(output_file)
    print(print_output)

def execute_command_with_output_and_print_and_print(user_input, output_file, print_output, print_output_and_print):
    # execute the command in the system using the os module
    os.system(user_input)
    with open(output_file, 'w') as f:
        f.write(output_file)
    print(print_output)
