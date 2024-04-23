import re
import os

with open('codegen_output.csv', 'r') as f:
    code_chunks = re.split(r'^\d+', f.read(), flags=re.MULTILINE)

for i, code in enumerate(code_chunks, start=1):
    code = code.strip()  # remove leading and trailing whitespace
    code = re.sub(r'^,', '', code)  # remove leading comma
    code = re.sub(r'^"', '', code)  # remove leading quote
    code = re.sub(r'"$', '', code)  # remove trailing quote

    if re.search(r'#include|typedef|struct|extern', code):  # C keywords
        ext = '.c'
    elif re.search(r'import|def|class|print', code):  # Python keywords
        ext = '.py'
    else:
        ext = '.unk'  # unknown language, use .unk extension

    # Create the 'src' directory if it doesn't exist
    if not os.path.exists('src'):
        os.makedirs('src')

    # Save the file in the 'src' directory
    with open(f'src/{i}{ext}', 'w') as output_file:
        output_file.write(code)
