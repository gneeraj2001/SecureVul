from flask import Flask, request
def evaluate_expression(request): # evaluate the input as a python expression and return the result
    expression = request.form['expression']
    result = eval(expression)
    return result

app = Flask(__name__)
app.config['SECRET_KEY'] ='secret'

@app.route('/evaluate', methods=['POST'])
def evaluate():
    return evaluate_expression(request)

if __name__ == '__main__':
    app.run(debug=True)