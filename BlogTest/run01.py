from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list')
def list():
    return render_template('list.html')

@app.route('/register',methods=['GET','POST'])
def register():
    referer = request.headers.get('Referer', '')
    if request.method == 'POST':
        for x in request.form:
            print(x,':',request.form[x])
    return render_template('register.html',params=locals())

@app.route('/login',methods=['GET','POST'])
def login():
    referer = request.headers.get('Referer', '')
    if request.method == 'POST':
        for x in request.form:
            print(x,':',request.form[x])
    return render_template('login.html',params=locals())


if __name__ == "__main__":
    app.run(debug=True,port=5200,host='0.0.0.0')