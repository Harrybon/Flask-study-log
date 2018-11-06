from flask import Flask

# 将当前程序构建成Flask 应用　以便结束用户请求并给出响应
app = Flask(__name__)

#　＠app.route() Flask中的路由定义 主要定义用户的访问路径　‘/’ 表示整个网站的根目录

@app.route('/')
#匹配上@app.route()路径后的处理程序－视图函数
def index():
    # return 响应给用户的内容
    return "<h1>hello world</h1>"

# 参数一个传递http://localhost:5000/show/xxx
@app.route('/show/<name>')
def show(name):
    if name == 'admin':
        return '传递的参数为%s'%name
    else:
        return "404 Not Found!"

# 带多个参数的路由http://localhost:5000/show/laowang/36
@app.route('/show/<name>/<int:age>')
def show_name_age(name,age):
    return '姓名:%s年龄:%s'%(name,age)

@app.route('/category')
@app.route('/cate')
def category():
    return '商品分类页面'

if __name__ == "__main__":
    # 启动Flask服务 默认本机开启端口　5000
    # app.run(debug=True port=5555) 设置端口为　5555
    # debug=True 将启动模式更改为调试模式(开发环境)　生产环境设置为false
    app.run(debug=True)