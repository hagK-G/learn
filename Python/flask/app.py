# pylint: disable=invalid-name
#coding=utf-8
# all imports

# import os
import config
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

main = '__main__'
DB_CONFIG = dict(
    type='sqlite_db',
    mode='r',
    file='schema.sql')
app = Flask(__name__)
app.config.from_object(config)


def connect_db():
    """使用 sqlite3.Row 表示数据库的行"""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    """首次调用时为当前环境创建数据库连接，调用成功后返回已建立好的连接"""
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext # 应用环境销毁时执行
def close_db(error):
    """应用环境在请求传入前创建，请求结束时销毁"""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

def init_db():
    """ 初始化数据库"""
    with app.app_context():
        """ g 在应用环境外无法获知它属于哪个应用，with app.app_context()建立了应用环境，g 对象会与 app 关联 """
        db = get_db()
        with app.open_resource(DB_CONFIG['file'], mode=DB_CONFIG['mode']) as f:
            db.cursor().executescript(f.read())
        """语句结束时释放关联并执行所有销毁函数"""
        db.commit()

if __name__ == main:
    """启动应用"""
    init_db()
    app.run(debug=app.config['DEBUG'])


@app.route('/')
def index():
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row(1)) for row in cur.fetchall()]
# print 'config is %s' % app.config['DATABASE']