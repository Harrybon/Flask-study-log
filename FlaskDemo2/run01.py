from flask import Flask, render_template, url_for

app = Flask(__name__)

class Person(object):
    name = None

    def say(self):
        return 'Hello Mrs. Tree'

#将01-template.html模板文件渲染成字符串后响应给客户端
@app.route('/01-template')
def template():
    # 将01-template.html渲染成字符串
    # html = render_template('01-template.html')
    # print(html)
    # return html
    # 渲染01-template.html，并传递变量
    # dic = {
    #     'name':'Simple happy',
    #     'Name':'《绿光》',
    #     'contens':'宝强',
    #     'music':'乃亮',
    #     'player':'羽凡',
    # }
    # return render_template('01-template.html',params=dic)
    # locals()将当前所有局部变量封装成一个字典
    name = 'Simple happy'
    Name = '绿光'
    contens = '宝强'
    music = '乃亮'
    player = '羽凡'
    # locals()将当前所有局部变量封装成一个字典
    print(locals())
    return render_template('01-template.html',params=locals())

# 能够传递到模板中作为变量的数据类型都有那些
@app.route('/02-var')
def var():
    uname = '  my name is Mrs. Tree'
    bookName = 'hello Mrs. Tree'
    auther = '宝强'
    price = 32.5
    list = ['hansonle','dijia','ATM']
    tuple = ('三国演义','西游记','红楼梦','水浒传')
    dict = {
        'a':1,
        'b':2,
        'c':3,
        'd':4,
    }
    person = Person()
    person.name = '宝强'
    print(locals())
    return render_template('02-var.html',params = locals())

# if 标签
@app.route('/03-if')
def tag():
    uname = ''
    return render_template('03-if.html',params=locals())

# 模拟登录地址
@app.route('/user/login')
def login():
    return '模拟登录中......'

@app.route('/04-for')
def for_views():
    list = ['猎空','麦克雷','Dva']
    dict = {
        'a':1,
        'b':2,
        'c':3,
        'd':4,
    }
    return render_template('04-for.html',params=locals())

@app.route('/05-static')
def static_views():
    return render_template('05-static.html')
if __name__ == '__main__':
    app.run(debug=True,port=5004)