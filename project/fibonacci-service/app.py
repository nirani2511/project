from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/fibonacci/<int:num>')
def fibonacci(num):
    if num == 0:
        return jsonify({'result': 0})
    elif num == 1:
        return jsonify({'result': 1})
    else:
        a, b = 0, 1
        for _ in range(num - 1):
            a, b = b, a + b
        return jsonify({'result': b})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
