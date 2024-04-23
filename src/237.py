from flask import Flask, request

def evaluate_code():
    if request.method == "POST":
        data = request.form["data"]
        result = eval(data)
        return str(result)
    else:
        return "Invalid request"

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/evaluate", methods=["POST"])
def evaluate():
    return evaluate_code()

if __name__ == "__main__":
    app.run(debug=True)