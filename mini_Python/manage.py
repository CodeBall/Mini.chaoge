from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
#初始化数据库连接
engine = create_engine('mysql+pymysql://root:BIG BEN@localhost/chaoge?charset=utf8')
#创建对象的基类
Base = declarative_base()

Session = sessionmaker()
Session.configure(bind=engine)

session = Session()

from view import *

# print(globals())

if __name__ == '__main__':
    app.run()
