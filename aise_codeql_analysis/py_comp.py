import os
import shutil
import py_compile

def has_syntax_errors(file_path):
    try:
        py_compile.compile(file_path, doraise=True)
    except py_compile.PyCompileError:
        return True
    return False

def move_files_with_syntax_errors(input_dir, output_dir):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Iterate through each file in the input directory
    for file_name in os.listdir(input_dir):
        file_path = os.path.join(input_dir, file_name)
        
        # Check if the file is a Python source file
        if file_name.endswith('.py'):
            # Check if the file has syntax errors
            if has_syntax_errors(file_path):
                # Move the file to the output directory
                shutil.move(file_path, os.path.join(output_dir, file_name))
                print(f"File '{file_name}' moved due to syntax errors.")
            else:
                print(f"File '{file_name}' is syntactically correct.")

# Example usage:
input_dir = "output"
output_dir = "files_with_syntax_errors"
move_files_with_syntax_errors(input_dir, output_dir)

