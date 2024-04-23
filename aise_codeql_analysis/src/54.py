import time
def evaluate_expression():
    # continuously ask user for expression, evaluate and print result with 1 second delay
    while True:
        expression = input(""Enter an expression: "")
        if expression == ""done"":
            break
        else:
            print(evaluate_expression.__name__ + ""("" + expression + "")"")
            time.sleep(1)
    print(""Done!"")

def evaluate_expression_with_time():
    # continuously ask user for expression, evaluate and print result with 1 second delay
    while True:
        expression = input(""Enter an expression: "")
        if expression == ""done"":
            break
        else:
            print(evaluate_expression_with_time.__name__ + ""("" + expression + "")"")
            time.sleep(1)
    print(""Done!"")

def evaluate_expression_with_time_and_print():
    # continuously ask user for expression, evaluate and print result with 1 second delay
    while True:
        expression = input(""Enter an expression: "")
        if expression == ""done"":
            break
        else:
            print(evaluate_expression_with_time_and_print.__name__ + ""("" + expression + ""