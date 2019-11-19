import datetime
import json
from flask import Flask, render_template, request, session


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    if session['logged_in']:
        route = 'index.email'
    else:
        route = 'login.html'
    return render_template(route)


@app.route('/index.html', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        session['logged_in'] = True
    return render_template('index.html', username=username, user_password=password)


@app.route('/signup.html', methods=['GET', 'POST'])
def signup():
    user_data = open("static/user_data.json", "a+")
    return render_template('signup.html')


if __name__ == '__main__':
   app.run()