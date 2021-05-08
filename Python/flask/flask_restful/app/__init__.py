# pylint: disable=invalid-name
#coding=utf-8

from flask import Flask, request, jsonify, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask.ext.restful import Api, Resource
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

app = Flask(__name__)

app.config.from_object(config)

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
