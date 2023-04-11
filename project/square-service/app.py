from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/square/<int:num>')
def square(num):
    return jsonify({'result': num**2})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
