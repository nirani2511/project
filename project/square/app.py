from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def square():
    num = int(request.args.get("num"))
    return str(num ** 2)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
