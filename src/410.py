import random
def divide_random_numbers():
    # generate two random numbers between 0 and 10, then divide the first number by the second number
    # print error message if there is an error during division, otherwise print the result
    try:
        a = random.random()
        b = random.random()
        c = a / b
        print(c)
    except ZeroDivisionError:
        print("Error: Division by zero")
    except ValueError:
        print("Error: Invalid input")

divide_random_numbers()

# +
# generate two random numbers between 0 and 10, then divide the first number by the second number
# print error message if there is an error during division, otherwise print the result
try:
    a = random.random()
    b = random.random()
    c = a / b
    print(c)
except ZeroDivisionError:
    print("Error: Division by zero")
except ValueError:
    print("Error: Invalid input")

# generate two random numbers between 0 and 10, then multiply the first number by the second number
# print error message if there is an error during multiplication, otherwise print the result
try:
    a = random.random()
    b = random.random()
    c = a * b
    print(c)
except ZeroDivisionError:
    print("Error: Division by zero")