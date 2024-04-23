import sqlite3
def login(username, password):
    # execute SQL query to select rows where username and password match
    passw = <PASSWORD>(password)
    c = sqlite3.connect('database.db')
    c.row_factory = sqlite3.Row
    cur = c.cursor()
    cur.execute("SELECT * FROM users WHERE username =? AND password =?", (username, passw))
    row = cur.fetchone()
    if row is not None:
        return row
    else:
        return None

def create_user(username, password):
    # execute SQL query to create a new user
    passw = <PASSWORD>(password)
    c = sqlite3.connect('database.db')
    c.row_factory = sqlite3.Row
    cur = c.cursor()
    cur.execute("INSERT INTO users (username, password) VALUES (?,?)", (username, passw))
    c.commit()
    c.close()

def create_post(title, content, username):
    # execute SQL query to create a new post
    c = sqlite3.connect('database.db')
    c.row_factory = sqlite3.Row
    cur = c.cursor