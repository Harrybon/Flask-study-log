from flask import Flask

app = Flask(__name__)

# http://localhost:5001/login
@app.route('/login')
def login():
    return "<h1>欢迎访问登录页面</h1>"

# http://localhost:5001/login
@app.route('/register',methods=['GET','POST'])
def register():
    return  '<h1 style="color:red">欢迎访问注册页面</h1>'

if __name__ == '__main__':
    app.run(debug=True,port=5001)