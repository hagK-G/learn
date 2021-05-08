# -*- coding: utf-8 -*-
# filename: manage.py
__author__ = 'milo zhao'
from flask_script import Manager
from app import app,db
from models import User
manager = Manager(app)
@manager.command
def save():
    user = User(3,'golang')
    db.session.add(user)
    db.session.commit()
@manager.command
def query_all():
    users = User.query.all()
    for user in users:
        print user
if __name__ == '__main__':
    manager.run()