from flask import Flask, request
def echo_data():
    # extract data field from POST request and return "Echo: [data]"
    data = request.form['data']
    return "Echo: " + data

app = Flask(__name__)
app.add_url_rule('/', 'index', echo_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)