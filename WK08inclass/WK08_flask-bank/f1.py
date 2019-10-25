# coding: utf-8
'''
运行在CMD中，进入f1.py所在的文件夹：
  SET FLASK_APP=f1.py
  flask run
  或者：python -m flask run
浏览器访问：http://127.0.0.1:5000
'''

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!<hr><a href="/hi">say hi</a>'

@app.route('/hi')
def hi():
    return 'Hello, World! from /hi'