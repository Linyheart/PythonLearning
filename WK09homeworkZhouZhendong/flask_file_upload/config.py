DEBUG = True
HOST = "127.0.0.1"
PORT = "3306"
DB = "harp"
USER = "root"
PASS = "Your Password"
CHARSET = "utf8"
DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset={}".format(USER, PASS, HOST, PORT, DB, CHARSET)
SQLALCHEMY_DATABASE_URI = DB_URI