import datetime
import json
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, session


app = Flask(__name__)


db = SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = 'users_info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    register_time = db.Column(db.DateTime, nullable=False, default=datetime.now())


db.create_all()


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
        session['username'] = username
        session['logged_in'] = True
    return render_template('index.html', username=username, user_password=password)


@app.route('/signup.html', methods=['GET', 'POST'])
def signup():
    user_data = open("static/user_data.json", "a+")
    return render_template('signup.html')


if __name__ == '__main__':
   app.run()