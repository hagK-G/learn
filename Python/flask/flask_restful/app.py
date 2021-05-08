# -*- coding: utf-8 -*-
# coding: utf-8

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql//root@localhost:3306/flask"
track_modifications = app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS',True)
db = SQLAlchemy(app)
@app.route('/')
def hello_world():
    return 'Hello World!'
if __name__ == '__main__':
    app.run(debug=True)