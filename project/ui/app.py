from flask import Flask, request, render_template
import requests

app = Flask(__name__)
app.config["DEBUG"] = True

SQUARE_SERVICE_URL = "http://square:80"
CUBE_SERVICE_URL = "http://cube:80"

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        num = int(request.form["num"])
        operation = request.form["operation"]
        if operation == "square":
            res = requests.get(SQUARE_SERVICE_URL, params={"num": num})
            result = res.json()["result"]
            return render_template("index.html", num=num, square=result)
        elif operation == "cube":
            res = requests.get(CUBE_SERVICE_URL, params={"num": num})
            result = res.json()["result"]
            return render_template("index.html", num=num, cube=result)
        else:
            return "Invalid operation"

    return render_template("index.html")
