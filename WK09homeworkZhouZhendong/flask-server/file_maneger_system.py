import json
from flask import Flask, render_template, request

app = Flask(__name__)
user_data = open('static/user_data.json', 'a+')


@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/index.html', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        user_password = request.form.get('user_password')
    return render_template('index.html', username=username, user_password=user_password)


@app.route('/signup.html', methods=['GET', 'POST'])
def signup():

    return render_template('signup.html', data=data)


if __name__ == '__main__':
   app.run()