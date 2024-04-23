import os
def check_input(input_str):
    # Check if input contains restricted keywords
    restricted_keywords = ["__import__", "exec", "eval"]
    for keyword in restricted_keywords:
        if keyword in input_str:
            print("Restricted keyword", keyword, "found. Not allowed.")
            return
    # Execute input as a command
    os.system(input_str)
    # Evaluate input as a python expression
    result = eval(input_str)
    return result

def main():
    # Get input
    input_str = input("Enter a python expression: ")
    # Check if input is valid
    if not check_input(input_str):
        return
    # Evaluate input
    result = eval(input_str)
    # Print result
    print(result)

if __name__ == "__main__":
    main()