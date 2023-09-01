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



#@app.route('/count/<parameter>')
#def mycount(parameter):
#    result_string = "\n".join(map(str, parameter))
#    for item in parameter:
#        print(item)
#    return result_string

#my_range = range(param)
#result = mycount(my_range)
##print("Resulting string:")
#print(result)



if __name__ == '__main__':
    app.run(port=5555, debug=True)
