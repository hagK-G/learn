import config
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash

app = Flask(__name__)


    
app.config.from_object(config)

def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

connect_db()

@app.route('/')
def index():
    return 'aaa %s' % app.config['DATABASE']


if __name__ == '__main__':
    app.run(debug=config.DEBUG)