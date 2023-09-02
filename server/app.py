#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def user(parameter):
    #parameter = 'hello'
    print(f'{parameter}') 
    return(f'{parameter}') 

@app.route('/count/<int:parameter>')
def mycount(parameter):
    if isinstance(parameter, int) and parameter >= 0:
        numbers = '\n'.join(map(str, range(parameter))) + '\n'
        return numbers
    else:
        return "Invalid parameter. Please provide a non-negative integer."



@app.route('/math/<parameters>/')
def mymath(parameters):
    # Split the parameters using '/' as the separator
    params = parameters.split('/')
    
    # Check if there are exactly three parameters (num1, operation, num2)
    if len(params) != 3:
        return "Invalid URL format. Use /math/num1/operation/num2"
    
    num1, operation, num2 = params
    
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return "Invalid number format. Use valid numbers."
    
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
            return "Division by zero is not allowed."
    elif operation == '%':
        if num2 != 0:
            result = num1 % num2
        else:
            return "Modulo by zero is not allowed."
    else:
        return "Invalid operation. Supported operations are +, -, *, div, and %."
    
    return f"Result: {result}"


# cant figure out this error
#    def test_math_route(self):
#        '''has a resource available at "/math/<parameters>".'''
#        response = app.test_client().get('/math/5/+/5')
#>       assert(response.status_code == 200)
#E       assert 404 == 200
#E        +  where 404 = <WrapperTestResponse streamed [404 NOT FOUND]>.status_code

#testing/app_test.py:51: AssertionError
#============================ short test summary info ==================================
#FAILED ../Flask application in flask_app.py has a resource available at "/math/<parameters>". - assert 404 == 200
#



if __name__ == '__main__':
    app.run(port=5555, debug=True)
