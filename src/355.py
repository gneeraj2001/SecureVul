from flask import Flask, request
def evaluate_expression(request): # evaluate the python expression received in the POST request using eval function and return the result
    try:
        expression = request.form['expression']
        result = eval(expression)
        return result
    except Exception as e:
        return str(e)

app = Flask(__name__)

@app.route('/evaluate', methods=['POST'])
def evaluate():
    return evaluate_expression(request)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)