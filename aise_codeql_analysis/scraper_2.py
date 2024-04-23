import csv

def extract_8th_column_and_write(csv_file, output_file):
    with open(csv_file, 'r', newline='') as file:
        with open(output_file, 'w', newline='') as output:
            reader = csv.reader(file)
            writer = csv.writer(output)
            
            # Iterate through each row in the CSV file
            for row in reader:
                # Check if the row has at least 8 columns
                if len(row) >= 8:
                    # Extract the content of the 8th column (index 7 in Python)
                    column_8 = row[8].strip()  # Assuming 0-based indexing
                    # Write the content of the 8th column to the output file
                    writer.writerow([column_8])
                else:
                    print("Row doesn't have 8 columns.")

# Example usage:
csv_file = "starcoder.csv"
output_file = "output.csv"
extract_8th_column_and_write(csv_file, output_file)

