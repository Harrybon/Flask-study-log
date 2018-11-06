from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:123456@localhost:3306/flask'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
db = SQLAlchemy(app)
# db.init_app(app)





class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(30), nullable=False)
    # 增加关联属性和反向引用关系
    teachers = db.relationship('Teacher',backref='course',lazy='dynamic')

    def __init__(self,cname):
        self.cname = cname

    def __repr__(self):
        return "Course{cname:%r}"%self.cname

class Student(db.Model):
    __tablename__ = 'student'
    id  = db.Column(db.Integer,primary_key=True)
    sname = db.Column(db.String(30),nullable=False)
    sage = db.Column(db.Integer)
    # course student 的多对多的实现
    # 增加关联属性及反向引用
    courses = db.relationship(
        'Course',
        secondary = 'student_course',
        lazy = 'dynamic',
        # 延迟动态加载
        backref = db.backref('students',lazy='dynamic')
    )

    # text
    teachers = db.relationship(
        'Teacher',
        secondary = 'student_teacher',
        lazy = 'dynamic',
        # 延迟动态加载
        backref = db.backref('students',lazy='dynamic')
    )





    def __repr__(self):
        return 'Student{sname: %s|sage: %s|}' % (self.sname, self.sage)


class Teacher(db.Model):
    __tablename__ = 'teacher'
    id  = db.Column(db.Integer,primary_key=True)
    tname = db.Column(db.String(30),nullable=False)
    tage = db.Column(db.Integer)
    # 增加外键列course_id 关联　course表
    course_id = db.Column(db.Integer,db.ForeignKey('course.id'))
    # 增加关联属性，反向引用
    wife = db.relationship('Wife',backref='teacher',uselist=False)

    def __repr__(self):
        return 'Teacher{tname: %s|tage: %s|}' % (self.tname, self.tage)


class Wife(db.Model):
    # __tablename__ = 'wife'
    id = db.Column(db.Integer,primary_key=True)
    wname = db.Column(db.String(30))
    wage = db.Column(db.Integer)
#     增加外键列，引用自Teacher
    teacher_id = db.Column(db.Integer,db.ForeignKey('teacher.id'))

    def __init__(self,wname,wage):
        self.wname = wname
        self.wage =wage

    def __repr__(self):
        return 'wife{wname:%r|wage:%r}'%(self.wname,self.wage)

# 创建第三张表(无需创建对应的实体类)
student_course = db.Table(
    #指定关联表的表名
    'student_course',
    db.Column('id',db.Integer,primary_key=True),
    db.Column('student_id',db.Integer,db.ForeignKey('student.id')),
    db.Column('course_id',db.Integer,db.ForeignKey('course.id'))
)

# text
student_teacher = db.Table(
    #指定关联表的表名
    'student_teacher',
    db.Column('id',db.Integer,primary_key=True),
    db.Column('student_id',db.Integer,db.ForeignKey('student.id')),
    db.Column('teacher_id',db.Integer,db.ForeignKey('teacher.id'))
)


db.create_all()


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/01-addcourse')
def add_course():
    course1 = Course('Python基础')
    course2 = Course('Python高级')
    course3 = Course('数据库基础')
    db.session.add_all([course1,course2,course3])
    print('ok')
    # db.session.add(course1)
    return ' insert ok'

@app.route('/02-register-teacher')
def register_teacher():
    teacher = Teacher()
    teacher.tname = 'Lv'
    teacher.tage = 25
    # course = Course.query.filter_by(id=3).first()
    teacher.course_id = 1
    db.session.add(teacher)
    return 'register ok'

@app.route('/03-query-teacher')
def query_teacher():
    #通过course 查找对应的老师
    course = Course.query.filter_by(id=1).first()
    print(course.cname)
    # 查找course对应的teacher
    teachers = course.teachers.all()
    print(teachers)
    # teacher-course
    teachers = Teacher.query.filter_by(id=1).first()
    course = teachers.course
    return 'query ok'

@app.route('/04-regTeacher',methods=['GET','POST'])
def regTeacher_views():
    if request.method =="GET":
        courses = Course.query.all()
        return render_template('regTeacher.html',courses=courses)
    else:
        tname = request.form.get('tname')
        tage = request.form.get('tage')
        course_id = request.form.get('course')
        teacher = Teacher()
        teacher.tname = tname
        teacher.tage = tage
        teacher.course_id = course_id
        db.session.add(teacher)
        return 'insert ok'

@app.route('/05-show')
def show_views():
    teachers = Teacher.query.all()
    return render_template('showtea.html',teachers =teachers)

@app.route('/06-regWife')
def reWife_views():
    # id赋值
    # wife = Wife('lili',18)
    # wife.teacher_id =2
    # 通过对象赋值
    wife = Wife('Bon',18)
    teacher = Teacher.query.filter_by(tname ='feng').first()
    wife.teacher = teacher
    db.session.add(wife)
    return 'insert ok'


@app.route('/07-querywife')
def querywife():
    # teacher 找wife
    teacher = Teacher.query.filter_by(id=1).first()
    wife =teacher.wife
    print(wife.wname)
    wife  = Wife.query.filter_by(id=2).first()
    teacher = wife.teacher
    print(teacher.tname)
    return 'query ok'

@app.route('/08-add-student-course')
def add_student_course():
    #获取ｉｄ＝１的学员信息
    student = Student.query.filter＿by(id=1).first()
    # 获取ｉｄ＝１的课程信息
    course = Course.query.filter_by(id=1).first()
    #将course student 关联
    student.courses.append(course)
    db.session.add(student)
    return 'Add course ok'

@app.route('/09-getM2M')
def getM2M():
    student = Student.query.filter＿by(id=1).first()
    courses = student.courses.all()
    print(courses)
    course = Course.query.filter_by(id =1).first()
    students = course.students.all()
    print(students)
    return 'query ok'

@app.route('/010-register-student',methods=['GET','POST'])
def register_student_views():
    if request.method == "GET":
        students  = Student.query.all()
        teachers  = Teacher.query.all()
        return render_template('registerStudent.html',students=students,teachers =teachers)
    else:
        sid =  request.form.get('sid')
        tids = request.form.getlist('tids')
        student = Student.query.filter_by(id =sid).first()
        teachers = Teacher.query.filter(Teacher.id.in_(tids)).all()
        for tea in teachers:
            student.teachers.append(tea)
        return 'register ok'

@app.route('/011-show')
def show_tea():
    students = Student.query.all()
    return render_template('showtea02.html',students = students)


if __name__ == '__main__':
    app.run(debug=True)
