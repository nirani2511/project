from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        number = request.form['number']
        operation = request.form['operation']
        url = f"http://{operation}:5000/{operation}?number={number}"
        response = requests.get(url)
        result = response.text
        return render_template('index.html', result=result)
    else:
        return render_template('index.html')
