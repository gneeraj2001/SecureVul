import os

# Define the directory path
directory = "rllm_src"

# Check if the directory exists
if os.path.exists(directory) and os.path.isdir(directory):
    # Iterate over each file in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            # Read the content of the file
            with open(filepath, 'r') as file:
                content = file.read()

            # Check if the content ends with the specific string
            specific_string = "<|endoftext|>"
            if content.endswith(specific_string):
                # Remove the specific string from the end of the content
                content = content[: -len(specific_string)]

                # Write the modified content back to the file
                with open(filepath, 'w') as file:
                    file.write(content)

                print(f'Removed "{specific_string}" from the end of {filename}')
            else:
                print(f'No "{specific_string}" found at the end of {filename}')
else:
    print(f"Directory '{directory}' does not exist or is not a directory.")

