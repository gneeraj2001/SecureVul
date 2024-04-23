import csv
import os

# Create a directory called "rllm_src" if it doesn't exist
directory = "rllm_src"
if not os.path.exists(directory):
    os.makedirs(directory)

# Open the CSV file for reading
with open('rllm_output.csv', newline='') as csvfile:
    # Specify the delimiter as double quotes
    csv_reader = csv.reader(csvfile, delimiter='"')

    # Iterate over each chunk in the CSV file
    for i, chunk in enumerate(csv_reader):
        # Remove leading double quote (") and trailing ^M
        cleaned_chunk = chunk[0].strip('"').replace('^M', '')

        # Check if the end of the chunk contains a specific string and remove it
        if cleaned_chunk.endswith("specific_string"):
            cleaned_chunk = cleaned_chunk[:-len("specific_string")]

        # Determine if the code chunk is CPP or Python
        is_cpp = any(line.startswith('#include') or line.startswith('using namespace') for line in cleaned_chunk.split('\n'))

        # Create a filename for the chunk based on the language
        filename = os.path.join(directory, f'chunk_{i}.{"cpp" if is_cpp else "py"}')

        # Write the cleaned chunk to the appropriate file
        with open(filename, 'w') as chunk_file:
            chunk_file.write(cleaned_chunk)

        print(f'Chunk {i} saved to {filename}')

