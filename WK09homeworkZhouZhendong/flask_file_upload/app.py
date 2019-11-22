import datetime
import os
from sqlalchemy import and_
from werkzeug.security import generate_password_hash, check_password_hash
import config
from flask import Flask, url_for, redirect, render_template, request, flash, session, \
    send_from_directory
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config)  # 导入config里的内容

db = SQLAlchemy(app)    # 初始化连接数据库


class Users(db.Model):  # 用户模型
    __tablename__ = 'users_info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    register_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())


class Files(db.Model):  # 文件模型
    __tablename__ = 'files_info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    filename = db.Column(db.String(100), nullable=False)
    file_description = db.Column(db.String(100), nullable=False)
    file_mime_type = db.Column(db.String(100), nullable=False)
    file_size = db.Column(db.Integer, nullable=False)
    upload_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users_info.id'), nullable=False)
    user = db.relationship('Users', backref=db.backref('Files', order_by=upload_time.desc()))


class Mime_types(db.Model): # MIME类型的模型
    __tablename__ = 'mime_type'
    name = db.Column(db.String(100), primary_key=True, nullable=False)
    template = db.Column(db.String(100), nullable=False)
    reference = db.Column(db.String(100), nullable=False)


db.create_all() # 初始化所有模型，每一个模型都对应数据库的一个的表格


def validate(username, password1, password2=None):  # 注册和登录时检查用户名和密码的合法性
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
            if check_password_hash(user.password, password1):   # 用hash值检验密码正确与否
                return '登录成功'
            else:
                return '密码错误'
        else:
            return '用户不存在'


@app.route('/', methods=['GET', 'POST'])    # 首页的视图
def home():
    if not session.permanent:   # 检查登录状态
        return redirect(url_for('login'))   # 未登录则跳转到登录界面
    else:
        return render_template('home.html', username=session['username'])   # 已登录则进入首页


@app.route('/register/', methods=['GET', 'POST'])   # 注册页面的视图
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        message = validate(username, password1, password2)  # 利用函数检查合法性
        flash(message)
        if '成功' in message:
            new_user = Users(username=username, password=generate_password_hash(password1)) # 新建用户
            db.session.add(new_user)    # 添加到session队列
            db.session.commit()     # 提交到数据库
            return redirect(url_for('login'))   # 注册成功则跳转到登录界面
        else:
            return render_template('register.html')     # 注册失败则回到注册界面


@app.route('/login/', methods=['GET', 'POST'])  # 登录页面的视图
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password1')
        message = validate(username, password)
        if '成功' in message:
            session['username'] = username  # 登陆成功则把登录状态记录到session里
            session.permanent = True
            return render_template('home.html', username=session['username'])   # 登陆成功回到首页
        else:
            flash(message)
            return render_template('login.html')    # 登录失败重新回到登录界面


@app.route('/logout/')  # 注销的视图
def logout():
    session.clear() # 注销则清楚session里的登录状态
    return redirect(url_for('home'))    # 注销成功，回到首页


@app.route('/upload', methods=['GET', 'POST'])  # 上传页面的视图
def upload():
    if not session.permanent:   # 检查登录状态
        flash("请先登录！")
        return redirect(url_for('login'))   # 未登录则弹出未登录通知且跳转到登录界面
    else:
        if request.method == 'POST':
            file = request.files['file']    # 获取文件上传请求
            base_path = os.path.abspath(os.path.dirname(__file__))  # 本文件的绝对路径
            upload_path = os.path.join(base_path, '_upload', session['username'])   # 上传的绝对路径
            if not os.path.exists(upload_path):     # 检查上传路径是否存在，不存在则新建路径
                os.makedirs(upload_path)
            file.filename = file.filename.replace(' ', '__blank__')     # 将文件名中的空格进行替换防止后续处理出错
            file_path = os.path.join(upload_path, file.filename)
            file.save(file_path)    # 保存文件
            if request.form.get('file_description'):    # 获取文件描述，若用户未填写文件描述则默认为文件名
                file_description = request.form.get('file_description')
            else:
                file_description = file.filename
            file_type = file.filename.split(".")[1]     # 根据文件名称获取文件扩展名
            mime_type = Mime_types.query.filter(Mime_types.name == file_type).first()   # 根据文件扩展名在数据库中获取MIME类型
            if not mime_type:   # 若数据库中MIME类型不包含上传文件的类型，则返回通知并删除已上传的文件，跳转到上传界面
                flash('不支持的文件类型！')
                os.remove(file_path)
                return render_template('upload.html')
            else:
                file_size = os.path.getsize(file_path)  # 获取文件大小
                user = Users.query.filter(Users.username == session['username']).first()    # 获取当前用户的模型用于获取文件对应的用户ID
                new_file = Files(filename=file.filename, file_description=file_description,
                                 file_mime_type=mime_type.template, file_size=file_size, user_id=user.id)   # 新建文件模型
                check_new_file_name = Files.query.filter(Files.filename == new_file.filename).first()       # 查找是否有同名文件
                check_new_file_user_id = Files.query.filter(Files.user_id == new_file.user_id).first()
                if check_new_file_name is None or check_new_file_user_id is None:   # 判断同一用户是否上传过同名文件
                    check_new_file = True
                else:
                    check_new_file = False
                if check_new_file:
                    db.session.add(new_file)    # 将文件模型添加到session队列
                    db.session.commit()
                    flash("文件上传成功！")
                else:
                    flash('文件已存在！')
                    return render_template('upload.html')   # 若文件已存在则回到上传界面
        return render_template('upload.html')   # 上传成功，回到上传界面


@app.route('/files', methods=['GET', 'POST'])   # 我的文件页面视图
def files():
    if not session.permanent:   # 检查登录状态
        flash("请先登录！")
        return redirect(url_for('login'))
    else:
        user = Users.query.filter(Users.username == session['username']).first()
        files = Files.query.filter(Files.user_id == user.id).all()
        if len(files) == 0:
            flash('没有文件，请上传！')      # 若用户未上传文件则会提示
        files_read_path = []    # 文件的在线预览、下载和删除链接的数组
        files_download_path = []
        files_delete_path = []
        for file in files:
            files_read_path.append("/read_file/?filename=/_upload/" + user.username + '/' + file.filename)
        for file in files:
            files_download_path.append("/download_file/?filename=/_upload/" + user.username + '/' + file.filename)
        for file in files:
            files_delete_path.append("/delete_file/?filename=/_upload/" + user.username + '/' + file.filename)
        for file in files:      # 将文件名和描述中的'__blank__'替换回空格
            file.filename = file.filename.replace('__blank__', ' ')
            file.file_description = file.file_description.replace('__blank__', ' ')
        for file in files:      # 将以字节为单位的大小转换为KB、MB和GB，且KB保留到整数，MB保留一位小数，GB保留两位小数
            if file.file_size > 1024 * 1024 * 1024:
                file.file_size = str(round(file.file_size / (1024 * 1024 * 1024), 2)) + 'GB'
            elif file.file_size > 1024 * 1024:
                file.file_size = str(round(file.file_size / (1024 * 1024), 1)) + 'MB'
            elif file.file_size > 1024:
                file.file_size = str(round(file.file_size / 1024)) + 'KB'
        return render_template('files.html', files=files, i=1, files_read_path=files_read_path,
                               files_download_path=files_download_path, files_delete_path=files_delete_path)


@app.route('/read_file/', methods=['GET', 'POST'])      # 预览文件的视图
def read_file():
    if request.method == 'GET':
        full_filename = request.args.get('filename')
        full_filename_list = full_filename.split('/')
        filename = full_filename_list[-1]
        file_path = os.path.join(app.root_path, '_upload', session['username'])
    return send_from_directory(file_path, filename=filename, as_attachment=False)


@app.route('/download_file/', methods=['GET', 'POST'])      # 下载文件的视图
def download_file():
    if request.method == 'GET':
        full_filename = request.args.get('filename')
        full_filename_list = full_filename.split('/')
        filename = full_filename_list[-1]
        file_path = os.path.join(app.root_path, '_upload', session['username'])
    return send_from_directory(file_path, filename=filename, as_attachment=True)


@app.route('/delete_file/', methods=['GET', 'POST'])        # 删除文件的视图
def delete_file():
    if request.method == 'GET':
        full_filename = request.args.get('filename')
        full_filename_list = full_filename.split('/')
        filename = full_filename_list[-1]
        delete_file_user = Users.query.filter(Users.username == session['username']).first()
        will_delete_file = Files.query.filter(and_(Files.filename == filename),
                                              (Files.user_id == delete_file_user.id)).first()
        db.session.delete(will_delete_file)     # 删除数据库数据
        db.session.commit()
        will_delete_file_path = os.path.join(app.root_path, '_upload', session['username'], filename)
        os.remove(will_delete_file_path)    # 删除本地文件
    return redirect(url_for('files'))


@app.context_processor
def my_context_processor():     # 传递参数的函数
    user = session.get('username')
    if user:
        return {'login_user': user}
    return {}


if __name__ == '__main__':
    app.run()
