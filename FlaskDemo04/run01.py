from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#为app指定数据库的配置信息
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/flask'
# 创建SQLAlchemy对象实例db，将app指定给实例
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True,port=5004)