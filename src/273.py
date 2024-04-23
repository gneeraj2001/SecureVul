import sys
def read_write_files(source_file, destination_file): # read content from source file and write into destination file
    with open(source_file, 'r') as f:
        content = f.read()
    with open(destination_file, 'w') as f:
        f.write(content)

def main():
    if len(sys.argv)!= 3:
        print("Usage: python3 write_file_to_file.py source_file destination_file")
        sys.exit(1)
    source_file = sys.argv[1]
    destination_file = sys.argv[2]
    read_write_files(source_file, destination_file)

if __name__ == '__main__':
    main()