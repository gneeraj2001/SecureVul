import time
def evaluate_user_input():
    # Continuously take user input, evaluate using eval() and print the result with a 1-second delay between each iteration
    while True:
        try:
            user_input = input("Enter a valid command: ")
            eval(user_input)
            time.sleep(1)
        except Exception as e:
            print("Error: {}".format(e))

# Evaluate user input
evaluate_user_input()