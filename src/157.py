import os
def unsafe_function():
    # take user input, evaluate using eval, and execute
    # the result
    return eval(input())

def main():
    # read the input
    input_file = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')
    input_lines = input_file.readlines()
    input_file.close()

    # evaluate the input
    result = unsafe_function()

    # write the output
    output_file = open(os.path.join(os.path.dirname(__file__), 'output.txt'), 'w')
    output_file.write(str(result))
    output_file.close()

if __name__ == '__main__':
    main()