from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/01-static')
def static_views():
    url = url_for('static',filename='images/b05.jpg')
    print(url)  #/static/images/b05.jpg
    return render_template('01-static.html')


@app.route('/02-parent')
def parent_views():
     return render_template('02-parent.html')

@app.route('/03-child')
def child_views():
     return render_template('03-child.html')

@app.route('/04-request')
def request_views():
    # print(dir(request))
    # scheme: 获取请求方案
    scheme = request.scheme
    # method: 获取请求方法
    method = request.method
    # args: 获取get请求方式提交的数据
    args = request.args
    # form: 获取post请求方式提交的数据
    form = request.form
    # cookies: 获取cookies的相关信息
    cookies = request.cookies
    # headers: 获取请求消息头的相关信息
    headers = request.headers
    referer = request.headers.get('Referer','')
    # files: 获取上传的文件
    # path: 获取请求的url地址（进入主机后的请求资源地址）
    path = request.path
    # full_path: 获取请求的url地址（进入主机后的请求资源地址，包含请求参数）
    full_path = request.full_path
    # url: 获取完整的请求地址，从协议: 开始
    url = request.url


    return render_template('04-request.html',params=locals())

@app.route('/05-form-get')
def form_get():
    return render_template('05-form-get.html')

@app.route('/06-get',methods=['GET'])
def get_views():
    print(request.args)
    print(request.args['upwd'])
    print(request.args.get('uname'))
    print(request.args.getlist('uname'))
    return 'get succeed'

@app.route('/07-form-post',methods=['POST','GET'])
def from_post():
    if request.method == 'GET':
        return render_template('07-post.html')
    elif request.method == 'POST':
        print(request.form)

if __name__ == '__main__':
    app.run(debug=True,port=5102,host='0.0.0.0')
