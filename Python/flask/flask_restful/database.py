# pylint: disable=invalid-name
#coding=utf-8

from flask import Flask, request, jsonify, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask.ext.restful import Api, Resource
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Fianna'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
api = Api(app)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(16), nullable=False, server_default='', unique=True)
    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32), nullable=False, unique=True, server_default='', index=True)
    password = db.Column(db.String(32), nullable=False, unique=True, server_default='', index=True)
    role_id = db.Column(db.Integer, nullable=False, server_default='0')
    def __repr__(self):
        return '<User %r,Role id %r>' %(self.username,self.role_id)
    def generate_tokey(self, expiration = 600):
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({id: self.id})
    @staticmethod
    def verify_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None # invalid token, but expired
        except BadSignature:
            return None # invalid token
        user = User.query.get(data['id'])
        return user


# FLASK RESTFUL API
class UserAPI(Resource):
    # def __init__(self, id):
        # if id is not None:
            # self.user = User.query.filter_by(id=id).first()
        # self.reqparse = reqparse.RequestParser()
        # self.reqparse.add_argument('username', type = str, location = 'json')
    def handle_username(self):
        if request.json['username'] is not None and request.json['password'] is not None
            self.username = request.json['username']
            self.password = request.json['password']
        else:
            abort(400)
            return 'username is required'
    def handle_id(self, id):
        if id is not None:
            self.user = User.query.filter_by(id=id).first()
    def get(self, id):
        self.handle_id(id)
        return dict(username=self.user.username, id=self.user.id, password=self.password)
    def delete(self, id):
        self.handle_id(id)
        db.session.delete(self.user)
        db.session.commit()
    def put(self, id):
        self.handle_id(id)
        self.handle_username()
        self.user.username = self.username
        db.session.commit()
        return 'update success'
    def post(self):
        self.handle_username()
        if User.query.filter_by(username = username).first() is not None:
            return 'existing user'
            abort(400)
        db.session.add(User(username=self.username, password=self.password))
        db.session.commit()
        return 'user %s created' % username 
        
class UserListAPI(Resource):
    def get(self):
        newList = []
        for  item in User.query.all():
            newList.append(dict(username=item.username, id=item.id))
        return jsonify(list=newList, total=len(newList))

api.add_resource(UserAPI, '/api/v1/users/<int:id>', endpoint='user')
api.add_resource(UserListAPI, '/api/v1/users', endpoint='users')

@app.route('/api/v1/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_tokey()
    return jsonify({'token': token.decode('ascii')})



# FLASK ROUTE API
# API_URI='/api/v1/'
# @app.route('/api/v1/user', methods=['POST'])
# def create_user():
#     username = request.json['username']
#     # password = request.json['password']
#     if username is None:
#     # if username is None or password is None:
#         return 'username is empty'
#         abort(400) # missing arguments
#     if User.query.filter_by(username = username).first() is not None:
#         return 'existing user'
#         abort(400) # existing user
#     db.session.add(User(username=username))
#     db.session.commit()
#     # print User.query.all()
#     return 'user %s created' % username 

# @app.route('/')
# def index():

# db.create_all() # create
# inject user
# db.session.add(Role(name='Moderator'))
# db.session.add(Role(name='User'))
# db.session.commit()

if __name__ == '__main__':
    """启动应用"""
    app.run(debug=True)
