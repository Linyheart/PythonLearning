import datetime
from flask import Flask, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = 'users_info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    register_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())


class Files(db.Model):
    __tablename__ = 'files_info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    filename = db.Column(db.String(100), nullable=False)
    file_description = db.Column(db.String(100), nullable=False)
    file_mime_type = db.Column(db.String(100), nullable=False)
    file_size = db.Column(db.Integer, nullable=False)
    upload_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    user_id = db.Column(db.Integer,db.ForeignKey('users_info.id'), nullable=False)
    user = db.relationship('Users', backref=db.backref('Files', order_by=upload_time.desc()))


db.create_all()


@app.route('/')
def index():
    # user = Users(username='Linyheart', password='linyheart')
    # db.session.add(user)
    # db.session.commit()
    # return render_template('home.html')
    # user = Users.query.filter(Users.id == 1).first()
    # print(user.username)
    # user.username = 'Linyhearts'
    # db.session.commit()
    # print(user.username)
    # return render_template('home.html')
    # file = Files(filename='Linyheart\'s first file.', file_description='Linyheart\'s first file.', file_mime_type='applicantion/json', file_size=10086)
    # db.session.add(file)
    # db.session.commit()
    # return render_template('home.html')
    # file = Files.query.filter(Files.id == 1).first()
    # file.user_id = 1
    # db.session.commit()
    return render_template('home.html')


if __name__ == '__main__':
    app.run()
