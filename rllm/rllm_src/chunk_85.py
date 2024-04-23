import os
import sys
def some_function():
    # try to execute the ls command using os.system method
    try:
        os.system("ls")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    some_function()