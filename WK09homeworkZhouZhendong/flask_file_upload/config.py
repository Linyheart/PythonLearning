DEBUG = True

HOST = "127.0.0.1"
PORT = "3306"
DB = "flaskFileSystem"  # 在MySQL数据库里建一个名称为这个的数据库，也可以修改名称
USER = "root"   # MySQL数据库用户名
PASS = "linyheart"  # 数据库密码
CHARSET = "utf8"
DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset={}".format(USER, PASS, HOST, PORT, DB, CHARSET)
SQLALCHEMY_DATABASE_URI = DB_URI

SECRET_KEY = "LINYHEART"    # 保存文件使用的密码,应该可以随意修改

UPLOAD_FOLDER = r'./_upload/'   # 上传文件的路径，可以随意修改
