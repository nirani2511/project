from flask import Flask, request, render_template
import requests

app = Flask(__name__)
app.config["DEBUG"] = True

SQUARE_SERVICE_URL = "http://square:80/square"
CUBE_SERVICE_URL = "http://cube:80/cube"

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        num = int(request.form["num"])
        operation = request.form["operation"]
        if operation == "square":
            result = requests.get(SQUARE_SERVICE_URL, params={"num": num}).text
        elif operation == "cube":
            result = requests.get(CUBE_SERVICE_URL, params={"num": num}).text
        else:
            result = "Invalid operation"
        return render_template("index.html", num=num, operation=operation, result=result)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
