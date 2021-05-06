from flask import Flask, request
app = Flask(__name__)

@app.route('/')

def index():
    return 'index'

@app.route('/hello')
def hello():
    return 'Hello World!'

@app.route('/post/<int:post_id>')
def post(post_id):
    return 'Post %d' % post_id

@app.route('/<name>')
def post_name(name):
    return 'Post name is %s' % name

@app.route('/<float:float>')
def float(float):
    return 'Float is %s' % float


@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        return 'CREATE USER'
    if request.method == 'GET':
        return 'GET USER'

@app.route('/user/')
def userDir():
    return 'user/'

if __name__ == '__main__':
    app.run(debug=True)