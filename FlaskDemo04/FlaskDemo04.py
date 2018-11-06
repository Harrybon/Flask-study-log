import time

import datetime
from flask import Flask, render_template, request, make_response,redirect
import os

from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/01-js')
def js_views():
    return render_template('01-js.html')

@app.route('/02-get')
def get_views():
    name = request.args['uname']
    age = request.args['uage']
    return name,age
##############################################

@app.route('/03-response')
def response_views():
    # resp = make_response('创建响应对象')
    resp = make_response(render_template('01-js.html'))
    return resp

# 重定向
@app.route('/04-redirect')
def redirect_views():
    redi = redirect('/01-js')
    # 通知浏览器向 '/01-js' 重新发送请求，然后再相应'/01-js'的内容
    return redi

# 文件的上传
@app.route('/05-file',methods=['GET','POST'])
def file_views():
    if request.method == 'GET':
        return render_template('05-file.html')
    else:
        f = request.files['uimg']
        print(f.filename)
        # 格式化输出当前时间
        ctime = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
        print('ctime-str:',ctime)
        fileNamelist = f.filename.split('.')
        filename = ctime+'.'+fileNamelist[len(fileNamelist)-1]
        print(filename)
        basepath = os.path.dirname(__file__)  # 当前执行文件所在路径
        upload_path = os.path.join(
            basepath,
            'static/upload/images',
            secure_filename(filename))
        # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f.save(upload_path)
        return 'upload ok'



if __name__ == '__main__':
    app.run(debug=True,port=5002,host='0.0.0.0')
