from flask import Flask, request
import operations


app = Flask(__name__)


@app.route('/add', methods=['GET'])
def addition():
    args = request.args
    a = args['a']
    a = int(a)
    b = args['b']
    b = int(b)
    answer = operations.add(a, b)

    return str(answer)


@app.route('/sub', methods=['GET'])
def subtraction():
    args = request.args
    a = args['a']
    a = int(a)
    b = args['b']
    b = int(b)
    answer = operations.sub(a, b)

    return str(answer)


@app.route('/mult', methods=['GET'])
def multiplication():
    args = request.args
    a = args['a']
    a = int(a)
    b = args['b']
    b = int(b)
    answer = operations.mult(a, b)

    return str(answer)


@app.route('/div', methods=['GET'])
def division():
    args = request.args
    a = args['a']
    a = int(a)
    b = args['b']
    b = int(b)
    answer = operations.div(a, b)

    return str(answer)
