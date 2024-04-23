import csv
import os

def save_content(content, index, output_dir):
    # Determine the file extension based on the content
    extension = ".cpp" if content.startswith("#include") or content.startswith("int main") else ".py"
    # Create the filename
    filename = os.path.join(output_dir, str(index) + extension)
    # Write the content to the file
    with open(filename, 'w') as file:
        file.write(content)

def split_csv_file(csv_file, output_dir):
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        
        # Skip the header row
        next(reader)
        
        # Iterate through each row in the CSV file
        for index, row in enumerate(reader, start=1):
            # Concatenate all columns into a single string
            content = "^M".join(row)
            # Save the content to a new file with the appropriate extension
            save_content(content, index, output_dir)

# Example usage:
csv_file = "output.csv"
output_dir = "output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
split_csv_file(csv_file, output_dir)

