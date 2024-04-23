import os
import shutil
import subprocess

def compile_cpp_file(file_path):
    # Compile the C++ file using g++ compiler
    process = subprocess.Popen(['g++', '-o', '/dev/null', file_path],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    _, error_output = process.communicate()
    
    # Check if there were any compilation errors
    if process.returncode != 0:
        return True, error_output.decode('utf-8')
    else:
        return False, ""

def move_files_with_errors(input_dir, output_dir):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Iterate through each file in the input directory
    for file_name in os.listdir(input_dir):
        file_path = os.path.join(input_dir, file_name)
        
        # Check if the file is a C++ source file
        if file_name.endswith('.cpp') or file_name.endswith('.cc') or file_name.endswith('.cxx'):
            # Compile the C++ file
            has_errors, error_output = compile_cpp_file(file_path)
            if has_errors:
                # Move the file to the output directory
                shutil.move(file_path, os.path.join(output_dir, file_name))
                print(f"File '{file_name}' moved due to compilation errors:")
                print(error_output)

# Example usage:
input_dir = "rllm_src"
output_dir = "files_with_errors"
move_files_with_errors(input_dir, output_dir)

