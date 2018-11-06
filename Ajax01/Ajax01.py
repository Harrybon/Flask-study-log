from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:123456@localhost:3306/ajax'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    loginname = db.Column(db.String(30),nullable=False)
    loginpwd = db.Column(db.String(30),nullable=False)
    uname = db.Column(db.String(30),nullable=False)

    def __init__(self,id,loginname,loginpwd,uname):
        self.loginname = loginname
        self.loginpwd = loginpwd
        self.uname = uname

# db.create_all()






@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/01-xhr')
def xhr_views():
    return render_template('01-xhr.html')

@app.route('/02-Ajax-get')
def Ajax_views():
    return render_template('02-ajax-get.html')

@app.route('/02-server')
def ajax_server():
    return '第一个AJAX请求'

@app.route('/02-server01')
def ajax_server01():
    return render_template('03-ajax-get.html')


@app.route('/02-server02')
def ajax_server02():
    res = request.args.get('uname')
    return '欢迎:'+res



@app.route('/04-post')
def post_ajax():
    return render_template('04-post.html')

@app.route('/04-server',methods=['POST'])
def server04():
    uname = request.form['uname']
    uage = request.form['uage']
    return '姓名：%s 年龄:%s'%(uname,uage)


@app.route('/06-register')
def register():
    return render_template('06-register.html')

@app.route('/06-server')
def server06():
    # 接受lname
    lname = request.args.get('lanme')
    user = Users.query.filter_by(loginname=lname).first()
    if user:
        return '用户名已存在'
    else:
        return '通过'



















if __name__ == '__main__':
    app.run(debug=True)
