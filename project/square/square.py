from flask import Flask, request

app = Flask(__name__)

@app.route('/square', methods=['GET'])
def square():
    number = request.args.get('number', default=0, type=int)
    result = number ** 2
    return str(result)

if __name__ == '__main__':
    app.run()
