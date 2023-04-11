from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num = int(request.form['num'])
        operation = request.form['operation']
        result = calculate(num, operation)
        return render_template('index.html', num=num, operation=operation, result=result)
    else:
        return render_template('index.html')

def calculate(num, operation):
    if operation == 'square':
        res = requests.get('http://square:80/square/{}'.format(num))
    elif operation == 'cube':
        res = requests.get('http://cube:80/cube/{}'.format(num))
    else:
        raise ValueError('Invalid operation: {}'.format(operation))
    res_data = res.json()
    if 'result' in res_data:
        return res_data['result']
    else:
        raise ValueError('Invalid response: {}'.format(res_data))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
