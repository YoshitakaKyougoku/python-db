'''
練習プログラム
'''

from bottle import Bottle,\
    jinja2_template as temprate,\
        static_file, request, redirect
        
from bottle import request, run
import psycopg2
import psycopg2.extras

#Bottleアプリ利用
app = Bottle()
@app.route('/', method=['GET', 'POST'])
def index():
    return "Hello World"
if __name__ == '__main__':
    run(app=app, host='0.0.0.0', port = '8888', reloader = True, debug = True)