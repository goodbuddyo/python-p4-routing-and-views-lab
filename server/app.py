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
    range_nums = []
    for i in range(parameter):
        range_nums.append(str(i))
        #if i < parameter:
        #    range_nums.append(str(i) + '\n')
        #else:
        #    range_nums.append(str(i))
        
    print(*range_nums, sep="\n")
            
    return range_nums
        


if __name__ == '__main__':
    app.run(port=5555, debug=True)
