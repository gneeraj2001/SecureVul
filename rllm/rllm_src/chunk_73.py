import sqlite3
def get_user_info(username):
    # connect to SQLite database
    # execute SQL query to fetch user info based on username
    # return the fetched data
    conn = sqlite3.connect('user_info.db')
    c = conn.cursor()
    c.execute("SELECT * FROM user_info WHERE username =?", (username,))
    user_info = c.fetchone()
    conn.close()
    return user_info

def get_user_info_by_id(id):
    # connect to SQLite database
    # execute SQL query to fetch user info based on id
    # return the fetched data
    conn = sqlite3.connect('user_info.db')
    c = conn.cursor()
    c.execute("SELECT * FROM user_info WHERE id =?", (id,))
    user_info = c.fetchone()
    conn.close()
    return user_info

def get_user_info_by_username(username):
    # connect to SQLite database
    # execute SQL query to fetch user info based on username
    # return the fetched data
    conn = sqlite3.connect('user_info.db')
    c = conn.cursor()
    c