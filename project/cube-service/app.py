from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/cube/<int:num>')
def cube(num):
    return jsonify({'result': num**3})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
