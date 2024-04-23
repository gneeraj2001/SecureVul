import sqlite3
def get_user_data(username):
    # query the users table in the database for a record where the username matches the provided username and return the user data
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username =?", (username,))
    user_data = c.fetchone()
    conn.close()
    return user_data

def get_user_data_by_id(id):
    # query the users table in the database for a record where the id matches the provided id and return the user data
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE id =?", (id,))
    user_data = c.fetchone()
    conn.close()
    return user_data

def get_user_data_by_username(username):
    # query the users table in the database for a record where the username matches the provided username and return the user data
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE