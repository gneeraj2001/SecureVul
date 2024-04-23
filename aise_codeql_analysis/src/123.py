import exec

def execute_python_code():
    # continuously ask user for Python code, execute it, and repeat
    while True:
        try:
            # ask user for input
            input_code = input(""Enter Python code: "")
            # execute it
            exec(input_code)
            # repeat
            continue
        except Exception as e:
            print(e)
            continue

def execute_python_code_with_return_value():
    # continuously ask user for Python code, execute it, and repeat
    while True:
        try:
            # ask user for input
            input_code = input(""Enter Python code: "")
            # execute it
            exec(input_code)
            # repeat
            return_value = eval(input_code)
            # repeat
            continue
        except Exception as e:
            print(e)
            continue

def execute_python_code_with_return_value_and_print():
    # continuously ask user for Python code, execute it, and repeat
    while True:
        try:
            # ask user for input
            input_code = input(""Enter Python code: "")
            # execute it
            exec(input_code)
            