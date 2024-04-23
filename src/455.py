from flask import Flask, request
def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello():
        user = request.args.get("user", "guest")
        return f"Hello, {user}"

    @app.route("/unsafe")
    def unsafe():
        user = request.args.get("user", "guest")
        result = eval(user)
        return result

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)