import sqlite3
def get_user_data(username):
    # query the users table in the database for a record where the username matches the provided username and return the user data
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute(""SELECT * FROM users WHERE username =?"", (username,))
    user_data = c.fetchone()
    conn.close()
    return user_data

def get_user_id(username):
    # query the users table in the database for a record where the username matches the provided username and return the user id
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute(""SELECT id FROM users WHERE username =?"", (username,))
    user_id = c.fetchone()
    conn.close()
    return user_id

def get_user_name(username):
    # query the users table in the database for a record where the username matches the provided username and return the user name
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute(""SELECT name FROM users WHERE username =?"", (username,))
    user_name = c.fetch