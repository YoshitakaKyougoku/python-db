'''
練習プログラム
'''

from bottle import Bottle,\
    jinja2_template as temprate,\
        static_file, request, redirect
        
from bottle import request, run
import psycopg2
import psycopg2.extras
import config

#DB connection
def get_connection():
    dsn = 'host={host} port={port} dbname={dbname} \
        user={user} password={password}'
    dsn = dsn.format(user = config.DB_USER, password = config.DB_PASS, \
        host = config.DB_HOST, port = config.DB_PORT, dbname = config.DB_NAME)
    return psycopg2.connect(dsn)
#Bottleアプリ利用
app = Bottle()
@app.route('/', method=['GET', 'POST'])
def index():
    return "Hello World"
if __name__ == '__main__':
    run(app=app, host='0.0.0.0', port = '8888', reloader = True, debug = True)