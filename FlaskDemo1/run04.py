from flask import Flask, url_for

app = Flask(__name__)
@app.route('/index')
def index():
    return '<h1>这是首页</h1>'

@app.route('/admin/login/form/show/<name>')
def show(name):
    return '参数值：%s'%name

@app.route('/url')
def url():
    #通过index() show(name) 反向解析路径
    url_index = url_for('index')
    url_show = url_for('show',name='haha')
    print(url_index,url_show)
    return url_index,url_show


if __name__ == "__main__":
    # 启动Flask服务 默认本机开启端口　5000
    # app.run(debug=True port=5555) 设置端口为　5555
    # debug=True 将启动模式更改为调试模式(开发环境)　生产环境设置为false
    app.run(debug=True,port=5001)