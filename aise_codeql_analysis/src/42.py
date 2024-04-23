from flask import Flask, request
def evaluate_expression(request): # evaluate the input as a python expression and return the result
    try:
        expression = request.form['expression']
        result = eval(expression)
        return result
    except:
        return ""Error: Invalid expression""

app = Flask(__name__)

@app.route('/')
def hello_world():
    return ""Hello World!""

@app.route('/add', methods=['POST'])
def add():
    try:
        first_number = request.form['first_number']
        second_number = request.form['second_number']
        result = int(first_number) + int(second_number)
        return str(result)
    except:
        return ""Error: Invalid expression""

@app.route('/sub', methods=['POST'])
def sub():
    try:
        first_number = request.form['first_number']
        second_number = request.form['second_number']
        result = int(first_number) - int(second_number)
        return str(result)
    except:
        return ""Error: Invalid expression""

@app.route('