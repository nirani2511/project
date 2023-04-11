from flask import Flask, request

app = Flask(__name__)

@app.route('/cube', methods=['GET'])
def cube():
    number = request.args.get('number', default=0, type=int)
    result = number ** 3
    return str(result)

if __name__ == '__main__':
    app.run()
