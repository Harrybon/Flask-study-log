from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
import pymysql
from sqlalchemy import or_, func

pymysql.install_as_MySQLdb()

app = Flask(__name__)
#为app指定数据库的配置信息
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/flask'
# 数据改变后自动提交
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# 创建SQLAlchemy对象实例db，将app指定给实例
db = SQLAlchemy(app)

# 创建模型类　User类
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(80),unique=True,nullable=False)
    age = db.Column(db.Integer,nullable=True)
    email = db.Column(db.String(120),unique=True)
    # def __str__(self):
    #     return 'User{username=%s,email=%s,age=%s,}' % (self.username, self.email,self.age)

    def __init__(self,username,age,email):
        self.username = username
        self.age = age
        self.email = email

    def __repr__(self):
        return 'User{username: %s|age: %s|email: %s}' % (self.username, self.age, self.email)


class Student(db.Model):
    __tablename__ = 'student'
    id  = db.Column(db.Integer,primary_key=True)
    sname = db.Column(db.String(30),nullable=False)
    sage = db.Column(db.Integer)


class Teacher(db.Model):
    __tablename__ = 'teacher'
    id  = db.Column(db.Integer,primary_key=True)
    tname = db.Column(db.String(30),nullable=False)
    tage = db.Column(db.Integer)


class Course(db.Model):
    __tablename__ = 'course'
    id  = db.Column(db.Integer,primary_key=True)
    cname = db.Column(db.String(30),nullable=False)




# 将创建好的实体类映射到数据库
db.create_all()



@app.route('/')
def hello_world():
    return 'Hello Flask!'


@app.route('/01-insert')
def insert_views():
    #创建users对象并赋值
    # user1 = User('Bon',20,'5205201314@qq.com')
    # user2 = User('Xqq',19,'211314@bb.com')
    #将对象通过db.session.add()插入到数据库
    # db.session.add(user1)
    # db.session.add(user2)
    #提交db.commit()
    # db.session.commit()
    return '插入成功'

# 登录注册信息插入数据库
@app.route('/02-register',methods=['GET','POST'])
def register_views():
    if request.method == 'GET':
        return render_template('02-register.html')
    else:
        username = request.form.get('uname')
        age = request.form.get('uage')
        email = request.form.get('uemail')
        user3 = User(username,age,email)
        db.session.add(user3)
        return '插入成功'

@app.route('/03-query')
def query_views():
    # 测试query函数
    # print(db.session.query(User))
    # print(db.session.query(User,Course))
    # print(db.session.query(User.username,User.email))

    # -----------------------------------
    # query = db.session.query(User)
    # ulist = query.all()
    # for user in ulist:
    #     print("username:%s,age:%s:,email:%s"%(user.username,user.age,user.email))
    # print(ulist)
    # print(query.first(),query.count())
    # ------------------------------------------------
    res1 = db.session.query(User).filter(User.age>18)
    # and
    res2 = db.session.query(User).filter(User.age > 18,User.id >2)
    # or_
    res3 = db.session.query(User).filter(or_(User.age > 18,User.id >2))
    print(res1.all())
    print(res2.all())
    print(res3.all())
    print(db.session.query(User).filter(User.id==2).all())
    print(db.session.query(User).filter(User.email.like('%qq%')).all())
    print(db.session.query(User).filter(User.id.in_([1,3])).all())
    print(db.session.query(func.sum(User.age).label('sum_age')))
    print(db.session.query(User).filter_by(id=2).all())
    print(db.session.query(User).limit(2).all())
    print(db.session.query(User).limit(2).offset(1).all())
    print(db.session.query(User).order_by('id desc').all())
    print(db.session.query(User).order_by('id ,age'))
    return 'Query Ok'
@app.route('/03-queryall')
def queryall_views():
    # query = db.session.query(User)
    # ulist = query.all()
    # Ulist = []
    # for user in ulist:
    #     ulist2 = [user.username, user.age, user.email]
    #     print(ulist2)
    #     Ulist.append(ulist2)
    # user1_name = Ulist[0][0]
    # user1_age = Ulist[0][1]
    # user1_email = Ulist[0][2]
    # return render_template('03-queryall.html',params=locals())
    query = db.session.query(User).all()
    return render_template('03-queryall.html',users = query)

@app.route('/04-modify/<int:user_id>',methods=['GET','POST'])
def modify_views(user_id):
    if request.method == 'GET':
        query = db.session.query(User)
        res = query.filter(User.id == user_id).all()
        print(res)
        return render_template('04-modify.html', users=res)
    else:
        Nname = request.form.get('uname')
        Nage = request.form.get('uage')
        Nemail = request.form.get('uemail')
        user = db.session.query(User).filter(User.username == Nname).first()
        print(user)
        user.username = Nname
        user.age = Nage
        user.email = Nemail
        print('修改成功')
        return redirect('/03-queryall')

# --------------------------------------------------

@app.route('/05-query')
def query05_views():
    # res = User.query.filter(User.id==1).first()
    res = User.query.filter_by(id = 2).first()
    print(res)
    return 'Query Ok'

@app.route('/06-delete/<int:user_id>')
def delete_views(user_id):
    res = User.query.filter_by(id=user_id).first()
    db.session.delete(res)
    return '删除成功'







if __name__ == '__main__':
    app.run(debug=True,port=5006,host='0.0.0.0')
