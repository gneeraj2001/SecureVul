import sqlite3
from flask import Flask, request
def get_user_details(username): # fetch user details from SQLite database based on username
    conn = sqlite3.connect('user_details.db')
    c = conn.cursor()
    c.execute(""SELECT * FROM user_details WHERE username =?"", (username,))
    user_details = c.fetchone()
    conn.commit()
    conn.close()
    return user_details

def get_user_details_by_email(email): # fetch user details from SQLite database based on email
    conn = sqlite3.connect('user_details.db')
    c = conn.cursor()
    c.execute(""SELECT * FROM user_details WHERE email =?"", (email,))
    user_details = c.fetchone()
    conn.commit()
    conn.close()
    return user_details

def get_user_details_by_username(username): # fetch user details from SQLite database based on username
    conn = sqlite3.connect('user_details.db')
    c = conn.cursor()
    c.execute(""SELECT * FROM user_details WHERE username =?"", (username,))
    user_details =