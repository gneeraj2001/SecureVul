from flask import Flask, request
app = Flask(__name__)
def hello_name():
    name = request.args.get("name")
    if name:
        return "Hello, {}!".format(name)
    else:
        return "Hello,!"

@app.route("/")
def hello():
    return hello_name()

if __name__ == "__main__":
    app.run(debug=True)