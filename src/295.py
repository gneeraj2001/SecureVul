from flask import Flask, request

def calculate_expression():
    if request.method == "POST":
        data = request.get_data(as_text=True)
        result = eval(data)
        return str(result)

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/calculate", methods=["POST"])
def calculate():
    return calculate_expression()

if __name__ == "__main__":
    app.run(debug=True)