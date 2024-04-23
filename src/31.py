import os
def evaluate_code(user_input):
    return eval(user_input)

def main():
    # Get the input
    input_file = open("input.txt", "r")
    input_lines = input_file.readlines()
    input_file.close()

    # Get the output
    output_file = open("output.txt", "w")
    output_file.write("Part 1: {}\n".format(evaluate_code(input_lines[0])))
    output_file.write("Part 2: {}\n".format(evaluate_code(input_lines[1])))
    output_file.close()

if __name__ == "__main__":
    main()