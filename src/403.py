import sqlite3
def check_credentials(username, password): # check if the given credentials match an entry in the database
    conn = sqlite3.connect('credentials.db')
    c = conn.cursor()
    c.execute('SELECT * FROM credentials WHERE username =? AND password =?', (username, password))
    result = c.fetchone()
    conn.close()
    if result is not None:
        return True
    else:
        return False

def create_credentials(username, password): # create a new entry in the database
    conn = sqlite3.connect('credentials.db')
    c = conn.cursor()
    c.execute('INSERT INTO credentials (username, password) VALUES (?,?)', (username, password))
    conn.commit()
    conn.close()

def save_credentials(username, password): # save the given credentials to the database
    conn = sqlite3.connect('credentials.db')
    c = conn.cursor()
    c.execute('SELECT * FROM credentials WHERE username =?', (username,))
    result = c.fetchone()
    if result is None:
        create_credentials(username, password)
    else:
        c.execute('UPDATE credentials SET password =? WHERE username =?', (password, username))
    conn.commit()
    conn.close()

def delete_credentials(username): # delete the given credentials from the database
    conn = sqlite