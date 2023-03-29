# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask
from flask import request

app =  Flask(__name__)

@app.route("/")
def hello_world1():
    return "<h1>Hello,World</h1>"


@app.route("/Hello,World1")
def hello_world2():
    return "<h1>Hello,World1</h1>"


@app.route("/test")
def test():
    return ("this is my function")

@app.route("/testnum")
def testnum():
    a = 5+6
    return "this is my function {}".format(a)
    


@app.route("/Hello,World2")
def hello_world3():
    return "<h1>Hello,World2</h1>"

#input

@app.route("/input")
def testinput():
    data = request.args.get('x')
    return 'this is data you have intered {}'.format(data)
    

if __name__=="__main__":
    app.run(host="0.0.0.0")
 
