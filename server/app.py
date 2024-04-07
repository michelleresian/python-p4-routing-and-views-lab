#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<int:parameter>')
def count(parameter):
    x = range(parameter)
    result = ""
    for n in x:
        result += str(n) + "\n"
    print(parameter)
    return result

@app.route('/math/<int:num1>/<string:operator>/<int:num2>')
def math(num1, operator, num2):
    if operator == '+':
        return str(num1 + num2)
    elif operator == '-':
        return str(num1 - num2)
    elif operator == '*':
        return str(num1 * num2)
    elif operator == 'div':
        return str(num1 / num2)
    elif operator == "%":
        return str(num1 % num2)
    else:
        return 'Invalid operation'



if __name__ == '__main__':
    app.run(port=5555, debug=True)