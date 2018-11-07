import json

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/ajax'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)



class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    loginname = db.Column(db.String(30),nullable=False)
    loginpwd = db.Column(db.String(30),nullable=False)
    uname = db.Column(db.String(30),nullable=False)

    def to_dict(self):
        dic = {
            'id':self.id,
            'loginname':self.loginname,
            'loginpwd':self.loginpwd,
            'uname':self.uname
        }
        return dic


class Province(db.Model):
    __tablename__ = 'province'
    id = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(30),nullable=False)














@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/01-allusers')
def allusers():
    return render_template('01-allusers.html')

@app.route('/01-server')
def server01():
    users = Users.query.all()
    return users

@app.route('/02-json')
def json_views():
    list = ['fan bing bing','li cheng']
    dict = {
        'name':'fan bing bing',
        'age':37,
        'gender':'female'
    }
    uList = [
        {
            'name': 'wang',
            'age': 37,
            'gender': 'male'
        },
        {
            'name': 'hang',
            'age': 27,
            'gender': 'female'
        }
    ]
    jsonStr1 = json.dumps(dict)
    jsonStr2 = json.dumps(list)
    jsonStr3 = json.dumps(uList)
    return (jsonStr1+'\n'+jsonStr2+jsonStr3)

@app.route('/02-html')
def html_views():
    return  render_template('02-json.html')

@app.route('/03-server')
def server03():
    uList = [
        {
            'name': 'wang',
            'age': 37,
            'gender': 'male'
        },
        {
            'name': 'hang',
            'age': 27,
            'gender': 'female'
        }
    ]
    return json.dumps(uList)

@app.route('/04-users')
def users04():
    return render_template('04-users.html')

@app.route('/04-server')
def server04():
    users = Users.query.all()
    l = []
    for u in users:
        l.append(u.to_dict())
    return json.dumps(l)

# ajax异步删除
@app.route('/04-delete')
def delete():
    #获取前端传递的id
    id = request.args.get('id')
    user = Users.query.filter_by(id=id).first()
    try:
        db.session.delete(user)
        dic = {
            'staus':1,
            'msg':'删除成功'
        }
    except Exception as e:
        print(e)
        dic = {
            'status':0,
            'msg':'删除失败,请联系管理员'
        }
    return json.dumps(dic)

# 级联显示
@app.route('/05-server05')
def server05():
    pass

















if __name__ == '__main__':
    app.run(debug=True,port=5004)
