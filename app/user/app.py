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

@app.route('/add', method=['GET', 'POST'])
def add():
    #user登録フォームのHTML
    form_html = """
    <head>登録フォーム</head>
    <body>
    <form action="/add" method="post">
    ユーザーID: <input type="text" name="user_id" value="<!--user_id-->" /><br /> 
    パスワード:<input type="text" name="passwd" value="<!--passwd-->" /><br /> 
    email:<input type="text" name="email" value="<!--email-->" /><br /> 
    氏:<input type="text" name="user_shi" value="<!--user_shi-->" /><br /> 
    名:<input type="text" name="user_mei" value="<!--user_mei-->" /><br /> 
    <input type="submit" value="" name="next"/>
    </form> 
    </body> 
    </html>
    """
    #ユーザー登録 確認画面のHTML
    confirm_html  = """
    <html> <head>確認</head>
    <body>
    <form action="/regist" method="post">
    ユーザーID: <!--user_id--><br /> 
    パスワード:<!--passwd--><br /> 
    email:<!--email--><br />
    氏:<!--user_shi--><br />
    名<!--user_mei--><br />
    <input type="hidden" name="user_id" value="<!--user_id-->" /> 
    <input type="hidden" name="passwd" value="<!--passwd-->" /> 
    <input type="hidden" name="email" value="<!--email-->" /> 
    <input type="hidden" name="user_shi" value="<!--user_shi-->" /> 
    <input type="hidden" name="user_mei" value="<!--user_mei-->" /> 
    <input type="submit" value="back" name="next" />&nbsp;&nbsp; 
    <input type="submit" value="regist" name="next"/>
    </form>
    </body>
    </html>
    """
    #GETでアクセスされたら
    if request.method == "GET" or request.forms.get('next') == 'back':
        return form_html.replace('<!--user_id-->', '').\
        replace('<!--passwd-->', '').\
        replace('<!--email-->', '').\
        replace('<!--user_shi-->', '').\
        replace('<!--user_mei-->', '')
    else:
        #postされたフォームの値を取得する
        form = {}
        form['user_id'] = request.forms.decode().get('user_id')
        form['passwd'] = request.forms.decode().get('passwd')
        form['email'] = request.forms.decode().get('email')
        form['user_shi'] = request.forms.decode().get('user_shi')
        form['user_mei'] = request.forms.decode().get('user_mei')
        
        if request.forms.get('next') == 'back':
            #戻る処理
            html = form_html
        else:
            #確認处理
            html = confirm_html
            #受け取った値を置換する
            #メソッドは重ね掛けできる
            
            return html.replace('<!--user_id-->', form['user_id']).\
            replace('<!--passwd-->', form['passwd']).\
            replace('<!--email-->', form['email']).\
            replace('<!--user_shi-->', form['user_shi']).\
            replace('<!--user_mei-->', form['user_mei'])
if __name__ == '__main__':
    run(app=app, host='0.0.0.0', port = '8888', reloader = True, debug = True)