from flask import Flask, request
def execute_code():
    # execute the code received through POST request using eval() function
    pass

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hello/<name>')
def hello(name):
    return 'Hello'+ name

@app.route('/hello/<name>/<int:age>')
def hello_name(name, age):
    return 'Hello'+ name +'' + str(age)

@app.route('/hello/<name>/<int:age>/<int:num>')
def hello_name_int(name, age, num):
    return 'Hello'+ name +'' + str(age) +'' + str(num)

@app.route('/hello/<name>/<int:age>/<int:num>/<int:num2>')
def hello_name_int_int(name, age, num, num2):
    return 'Hello'+ name +'' + str(age) +'' + str(num) +'' + str(num2)
