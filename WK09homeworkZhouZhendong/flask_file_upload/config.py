DEBUG = True

HOST = "127.0.0.1"
PORT = "3306"
DB = "flaskFileSystem"
USER = "root"
PASS = "linyheart"
CHARSET = "utf8"
DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset={}".format(USER, PASS, HOST, PORT, DB, CHARSET)
SQLALCHEMY_DATABASE_URI = DB_URI

SECRET_KEY = "LINYHEART"

UPLOAD_FOLDER = r'./_upload/'
