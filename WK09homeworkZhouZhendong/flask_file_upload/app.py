import datetime

from werkzeug.security import generate_password_hash, check_password_hash

import config
from flask import Flask, url_for, redirect, render_template, request, flash, session
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = 'users_info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    register_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    #
    # def __init__(self, *args, **kwargs):
    #     self.username = kwargs.get('username')
    #     self.password = generate_password_hash(kwargs.get('password'))


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


# def validate(username, password1, password2=None):
#     user = Users.query.filter(Users.username == username).first()
#     if password2:
#         if len(username) <= 0:
#             return '请输入用户名'
#         elif len(password1) <= 0:
#             return '请输入密码'
#         else:
#             if user:
#                 return '用户名已经存在'
#             else:
#                 if len(username) < 4:
#                     return '用户名长度至少4个字符'
#                 elif password1 != password2:
#                     return '两次密码不一致'
#                 elif len(password1) < 6:
#                     return '密码长度至少6个字符'
#                 else:
#                     return '注册成功'
#     else:
#         if len(username) <= 0:
#             return '请输入用户名'
#         elif len(password1) <= 0:
#             return '请输入密码'
#         else:
#             if user:
#                 if check_password_hash(user.password, password1):
#                     return '登录成功'
#                 else:
#                     return '密码错误'
#             else:
#                 if len(password2) <= 0:
#                     return '请再次输入密码'
#                 else:
#                     return '用户不存在'


def validate(username, password1, password2=None):
    user = Users.query.filter(Users.username == username).first()
    if password2:
        if user:
            return '用户名已经存在'
        else:
            if len(username) < 4:
                return '用户名长度至少4个字符'
            elif password1 != password2:
                return '两次密码不一致'
            elif len(password1) < 6:
                return '密码长度至少6个字符'
            else:
                return '注册成功，请登录'
    else:
        if user:
            if check_password_hash(user.password, password1):
            # if user.password == password1:
                return '登录成功'
            else:
                return '密码错误'
        else:
            return '用户不存在'


@app.route('/')
def home():
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


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        message = validate(username, password1, password2)
        flash(message)
        if '成功' in message:
            new_user = Users(username=username, password=generate_password_hash(password1))
            # new_user = Users(username=username, password=password1)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
        else:
            return render_template('register.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password1')
        message = validate(username, password)
        if '成功' in message:
            session['username'] = username
            session.permanent = True
            return render_template('home.html', login_message=message)
        else:
            flash(message)
            return render_template('login.html')


@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('home'))


# @app.context_processor
# def my_context_processor():
#     status = session.get('status', '')
#     return {'status': status}


@app.context_processor
def my_context_processor():
    user = session.get('username')
    if user:
        return {'login_user': user}
    return {}


if __name__ == '__main__':
    app.run()
