import sqlite3
from flask import Flask, request
def login():
    # fetch username and password from request arguments
    # connect to SQLite database
    # construct SQL query to select rows where username and password match
    # return appropriate message based on query result
    username = request.args.get('username')
    password = request.args.get('password')
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute(""SELECT * FROM users WHERE username =? AND password =?"", (username, password))
    row = c.fetchone()
    conn.commit()
    conn.close()
    if row:
        # if username and password match, return user details
        return jsonify(row)
    else:
        # if username and password don't match, return error message
        return jsonify('Invalid username or password'), 401

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the API'

@app.route('/users', methods=['GET'])
def get_users():
    # fetch all users from the database
    # return appropriate message based on query result
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute(""SELECT * FROM users"")
