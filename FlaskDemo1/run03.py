from flask import Flask

app = Flask(__name__)
@app.route('/')
@app.route('/index')
@app.route('/<int:num>')
@app.route('/index/<int:num>')
def index(num=1):
        return 'num:%d'%num
@app.route('/post',methods=['POST'])
def post():
    return '只接受post请求'

if __name__ == '__main__':
    app.run(debug=True,port=5002)

