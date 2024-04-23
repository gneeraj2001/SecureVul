import time
def passwordChecker(predefined_password): 
    # function to check if user input password matches predefined password 
    pass_check = True
    if predefined_password == """":
        print(""Please enter a password"")
        pass_check = False
    elif len(predefined_password) < 8:
        print(""Password must be at least 8 characters long"")
        pass_check = False
    elif predefined_password.isalpha() == False:
        print(""Password must contain only letters"")
        pass_check = False
    elif predefined_password.isdigit() == False:
        print(""Password must contain only digits"")
        pass_check = False
    elif predefined_password.isalnum() == False:
        print(""Password must contain only letters and digits"")
        pass_check = False
    else:
        print(""Password is valid"")
        pass_check = True
    return pass_check

def password_generator(length):
    # function to generate a random password
    password = """"
    for i in range(length):
        password += random.choice(string.ascii_letters)
    return password

def password_generator_2(length):
    #