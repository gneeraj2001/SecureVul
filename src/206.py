from flask import Flask, request

def evaluate_expression():
    # extract expression from JSON data, evaluate it and return result as string
    expression = request.get_json()['expression']
    result = eval(expression)
    return str(result)

app = Flask(__name__)

@app.route('/evaluate', methods=['POST'])
def evaluate():
    return evaluate_expression()

if __name__ == '__main__':
    app.run(debug=True)