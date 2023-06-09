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
        square = requests.get(SQUARE_SERVICE_URL, params={"num": num}).text
        cube = requests.get(CUBE_SERVICE_URL, params={"num": num}).text
        return render_template("index.html", num=num, square=square, cube=cube)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
