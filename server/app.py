#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# Index view
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Print string view
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  # Print the string to the console
    return parameter  # Return the string as plain text

# Count view
@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = '\n'.join(str(i) for i in range(parameter + 1))
    return numbers  # Return the numbers as plain text with newlines

# Math view
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            result = 'Error: Division by zero'
    elif operation == '%':
        result = num1 % num2
    else:
        result = 'Error: Unsupported operation'
    
    if isinstance(result, (int, float)):
        return str(result)  
    else:
        return result  

if __name__ == '__main__':
    app.run(port=5555, debug=True)