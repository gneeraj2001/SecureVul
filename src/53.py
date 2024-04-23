from flask import Flask, request

def execute_code():
    # extract code from POST request and execute using eval()
    return "Code executed"

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute():
    return execute_code()

if __name__ == '__main__':
    app.run(debug=True)