import sqlite3
from flask import Flask, request

def login():
    # route to handle login POST requests
    pass

def create_db():
    # create a database connection
    conn = sqlite3.connect('data.db')
    # create a cursor
    c = conn.cursor()
    # create a table
    c.execute(""""""CREATE TABLE IF NOT EXISTS users
                (username text, password text)"""""")
    # commit the changes
    conn.commit()
    # close the connection
    conn.close()

def insert_user(username, password):
    # create a database connection
    conn = sqlite3.connect('data.db')
    # create a cursor
    c = conn.cursor()
    # execute the INSERT statement
    c.execute(""INSERT INTO users VALUES (:username, :password)"",
              {'username': username, 'password': password})
    # commit the changes
    conn.commit()
    # close the connection
    conn.close()

def get_user(username):
    # create a database connection
    conn = sqlite3.connect('data.db')
    # create a cursor
    c = conn.cursor()