import os
def unsafe_function(user_input):
    # evaluate user input as Python code
    return eval(user_input)

def main():
    # read input from stdin
    user_input = input()
    # evaluate user input as Python code
    result = unsafe_function(user_input)
    # print result
    print(result)

if __name__ == '__main__':
    main()