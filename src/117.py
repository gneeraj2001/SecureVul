import os
from flask import Flask, request
def execute_system_command(request): # extract data from POST request and execute it as a system command
    command = request.form['command']
    if command == 'ls':
        return_value = os.popen(command).read()
        return return_value
    else:
        return_value = os.popen(command).read()
        return return_value

app = Flask(__name__)

@app.route('/execute_system_command', methods=['POST'])
def execute_system_command_post():
    return execute_system_command(request)

if __name__ == '__main__':
    app.run(debug=True)