import time
def evaluate_expression():
    # continuously ask user for expression, evaluate and print result with 1 second delay
    while True:
        expression = input("Enter expression: ")
        if expression == "exit":
            break
        time.sleep(1)
        result = evaluate(expression)
        print(result)

if __name__ == "__main__":
    evaluate_expression()