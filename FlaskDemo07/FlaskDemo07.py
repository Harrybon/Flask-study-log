from flask import Flask, make_response, request, session, render_template,redirect

app = Flask(__name__)
app.config['SECRET_KEY']='ai!#@$#3^$#4V45Dw6xdstcdEQ@!#@123534'

@app.route('/index')
def hello_world():
    return render_template('index.html')

@app.route('/01-setCookie')
def cookie_views():
    resp = make_response('添加cookie成功')
    resp.set_cookie('uname','rose',60*60*24*365)
    return resp

@app.route('/01-setCookie01')
def cookie_views01():
    resp = make_response('添加cookie02成功')
    resp.set_cookie('uname','rose',60)
    return resp

@app.route('/02-getCookie')
def getCookie_views():
    res = request.cookies
    print(res)
    return 'ok'


@app.route('/03-setSession')
def setSession():
    session['uname']  = 'wang'
    return 'set session success'

@app.route('/04-getSession')
def getSession():
    uname = session.get('uname','')
    if uname:
        return '用户名：'+uname
    else:
        return 'No Match'

# 登录页
@app.route('/login',methods=['GET','POST'])
def login_views():
    if request.method == 'GET':
        if 'uname' in session:
            return redirect('/index')
        else:
            if 'uname' in request.cookies:
                uname = request.cookies.get('uname')
                session['uname'] = uname
                return redirect('/index')
            else:
                return render_template('login.html')
    else:
        uname = request.form.get('uname')
        upwd = request.form.get('upwd')
        if uname  == 'admin' and upwd == 'admin':
            session['uname'] = uname
            if 'isSaved' in request.form:
                resp = redirect('/index')
                resp.set_cookie('uname',uname,60*60*24)
                return resp
        else:
            return redirect('/index')




if __name__ == '__main__':
    app.run(debug=True,port=5102)
