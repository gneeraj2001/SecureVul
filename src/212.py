import sqlite3
def get_user_info(username):
    # retrieve user information from the database based on the given username
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username =?', (username,))
    user_info = c.fetchone()
    conn.close()
    return user_info

def get_user_id(username):
    # retrieve user id from the database based on the given username
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT id FROM users WHERE username =?', (username,))
    user_id = c.fetchone()
    conn.close()
    return user_id

def get_user_info_by_id(user_id):
    # retrieve user information from the database based on the given user id
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE id =?', (user_id,))
    user_info = c.fetchone()
    conn.close()
    return user_info

def get_user_id_by_username(username):
    # retrieve user id from the database based on the given username
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c