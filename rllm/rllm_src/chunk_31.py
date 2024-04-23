import os
def evaluate_code(user_input):
    return eval(user_input)

def main():
    # Get the input
    user_input = input("Enter your code: ")
    # Evaluate the code
    result = evaluate_code(user_input)
    # Print the result
    print(result)

if __name__ == "__main__":
    main()