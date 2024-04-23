#!/bin/bash

# Set the folder containing the files to analyze
input_folder="$(pwd)/src"

# Create the output folder if it doesn't exist
mkdir -p output
mkdir -p db

# Loop through each file in the input folder
for file in "$input_folder"/*; do
    # Check if the file is a regular file
    if [ -f "$file" ]; then
        # Get the file name and extension
        filename=$(basename -- "$file")
        filename_no_ext="${filename%.*}"
        extension="${file##*.}"
        db="${filename_no_ext}_db"
	# Access the file
        echo "Analyzing file: $file"
        
        # Run CodeQL analysis based on file extension
        if [ "$extension" == "py" ]; then
            # Run CodeQL analysis for Python
            codeql database create $db -l=python -c "python3 $file" --overwrite
            codeql database analyze $db  python-code-scanning.qls --format=sarif-latest --output="output/$filename_no_ext.sarif"
			codeql database finalize $(pwd)/db/$db	
        elif [ "$extension" == "c" ] || [ "$extension" == "cpp" ]; then
            # Run CodeQL analysis for C/C++
			codeql database create $(pwd)/db/$db -l=cpp -c "g++ $file -o output/$filename_no_ext-exe" --overwrite

			codeql database analyze $(pwd)/db/$db cpp-code-scanning.qls --format=sarif-latest --output="output/$filename_no_ext.sarif"
			codeql database finalize $(pwd)/db/$db	
		else
            echo "Unsupported file extension: $extension"
            continue
        fi
        
        echo "Analysis complete for: $filename"
    fi
done
mv *_db db/
find $(pwd)/output ! -name "*.sarif" -delete
echo "All files analyzed."

