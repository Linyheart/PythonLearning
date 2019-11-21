import datetime
import os

from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

import config
from flask import Flask, url_for, redirect, render_template, request, flash, session, Response
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
    user_id = db.Column(db.Integer, db.ForeignKey('users_info.id'), nullable=False)
    user = db.relationship('Users', backref=db.backref('Files', order_by=upload_time.desc()))


class Mime_types(db.Model):
    __tablename__ = 'mime_type'
    name = db.Column(db.String(100), primary_key=True, nullable=False)
    template = db.Column(db.String(100), nullable=False)
    reference = db.Column(db.String(100), nullable=False)


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


@app.route('/', methods=['GET', 'POST'])
def home():
    # mime_type = Mime_types.query.filter(Mime_types.name == 'zip').first()
    # print(mime_type.template)
    if not session.permanent:
        return redirect(url_for('login'))
    else:
        return render_template('home.html', username=session['username'])


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
            return render_template('home.html', username=session['username'])
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


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if not session.permanent:
        flash("请先登录！")
        return redirect(url_for('login'))
    else:
        if request.method == 'POST':
            file = request.files['file']
            base_path = os.path.abspath(os.path.dirname(__file__))
            upload_path = os.path.join(base_path, '_upload', session['username'])
            print(upload_path)
            if not os.path.exists(upload_path):
                os.makedirs(upload_path)
            file_path = os.path.join(upload_path, file.filename)
            file.save(file_path)
            if request.form.get('file_description'):
                file_description = request.form.get('file_description')
            else:
                file_description = file.filename
            print(file_description)
            file_type = file.filename.split(".")[1]
            print(file_type)
            # file_type = os.path.splitext(file)[-1][1:]
            mime_type = Mime_types.query.filter(Mime_types.name == file_type).first()
            if not mime_type:
                flash('不支持的文件类型！')
                os.remove(file_path)
                return render_template('upload.html')
            else:
                print(mime_type.template)
                file_size = os.path.getsize(file_path)
                user = Users.query.filter(Users.username == session['username']).first()
                new_file = Files(filename=file.filename, file_description=file_description,
                                 file_mime_type=mime_type.template, file_size=file_size, user_id=user.id)
                check_new_file_name = Files.query.filter(Files.filename == new_file.filename).first()
                check_new_file_user_id = Files.query.filter(Files.user_id == new_file.user_id).first()
                print(check_new_file_user_id)
                print(check_new_file_name)
                if check_new_file_name is None or check_new_file_user_id is None:
                    check_new_file = True
                else:
                    check_new_file = False
                if check_new_file:
                    db.session.add(new_file)
                    db.session.commit()
                    print(check_new_file)
                    flash("文件上传成功！")
                else:
                    flash('文件已存在！')
                    print(check_new_file)
                    return render_template('upload.html')
        return render_template('upload.html')


@app.route('/files', methods=['GET', 'POST'])
def files():
    if not session.permanent:
        flash("请先登录！")
        return redirect(url_for('login'))
    else:
        user = Users.query.filter(Users.username == session['username']).first()
        files = Files.query.filter(Files.user_id == user.id).all()
        if len(files) == 0:
            flash('您没有上传过文件！')
        files_path = []
        for file in files:
            files_path.append("../_upload/" + user.username + '/' + file.filename)
        print(files_path)
        for file in files:
            if file.file_size > 1024 * 1024 * 1024:
                file.file_size = str(round(file.file_size / (1024 * 1024 * 1024), 2)) + 'GB'
            elif file.file_size > 1024 * 1024:
                file.file_size = str(round(file.file_size / (1024 * 1024), 1)) + 'MB'
            elif file.file_size > 1024:
                file.file_size = str(round(file.file_size / 1024)) + 'KB'
        return render_template('files.html', files=files, i=1, files_path=files_path)


@app.route('/download_file/', methods=['GET', 'POST'])
def download_file():
    if request.method == 'GET':
        full_filename = request.args.get('filename')
        full_filename_list = full_filename.split('/')
        filename = full_filename_list[-1]
        filepath = full_filename.replace('/%s' % filename, '')

        def send_file():
            store_path = full_filename
            with open(store_path, 'rb') as targetfile:
                while 1:
                    data = targetfile.read(20 * 1024 * 1024)  # 每次读取20M
                    if not data:
                        break
                    yield data

        response = Response(send_file(), content_type='application/octet-stream')
        response.headers["Content-disposition"] = 'attachment; filename=%s' % filename  # 如果不加上这行代码，导致下图的问题
        return response


@app.context_processor
def my_context_processor():
    user = session.get('username')
    if user:
        return {'login_user': user}
    return {}


@app.template_filter('asc')
def asc(i):
    i = i + 1
    return i


if __name__ == '__main__':
    app.run()
