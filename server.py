from flask import Flask, request

app = Flask(__name__)


@app.route("/test", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print(request.json)
    return "Hello World"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
