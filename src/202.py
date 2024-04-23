import time
def execute_python_code():
    # continuously ask user to enter Python code and execute it with a pause of one second after each execution
    while True:
        code = input("Enter Python code: ")
        if code == "exit":
            break
        time.sleep(1)
        try:
            exec(code)
        except Exception as e:
            print(e)

execute_python_code()