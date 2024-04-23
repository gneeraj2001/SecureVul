import os
def execute_user_input():
    # take user input, evaluate using eval, and execute it
    while True:
        try:
            user_input = input(""Enter a command: "")
            if user_input == ""exit"":
                break
            else:
                eval(user_input)
        except Exception as e:
            print(e)

def eval(user_input):
    # eval function
    if user_input.startswith(""print""):
        print(eval(user_input.split("" "")[1]))
    elif user_input.startswith(""if""):
        if eval(user_input.split("" "")[1]) == True:
            print(""true"")
        else:
            print(""false"")
    elif user_input.startswith(""while""):
        while eval(user_input.split("" "")[1]) == True:
            print(""true"")
        else:
            print(""false"")
    elif user_input.startswith(""for""):
        for i in range(eval(user_input.split("" "")[1])):
            print(i)
    elif user_input.startswith