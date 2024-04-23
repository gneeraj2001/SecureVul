import logging
def authenticate_user(username, password, users): 
    # Check if the entered username and password match any of the created users
    pass_match = False
    for user in users:
        if username == user['username'] and password == user['password']:
            pass_match = True
            break
    return pass_match

def create_user(username, password, users):
    # Create a new user
    new_user = {
        'username': username,
        'password': password
    }
    users.append(new_user)

def login(username, password, users):
    # Check if the entered username and password match any of the created users
    pass_match = False
    for user in users:
        if username == user['username'] and password == user['password']:
            pass_match = True
            break
    return pass_match

def create_user_with_password(username, password, users):
    # Create a new user
    new_user = {
        'username': username,
        'password': password
    }
    users.append(new_user)

def create_user_with_username(username, password, users):
    # Create a new user
    new_