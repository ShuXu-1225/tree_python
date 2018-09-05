## WSGI:
# from wsgiref.simple_server import make_server
# from hi import application
#
# httpd = make_server('', 8888, application)
# print('serving HTTP port 8888')
# httpd.serve_forever()
#

# # web框架 flask:
# from flask import Flask
# from flask import request
# from flask import render_template
#
# app = Flask(__name__)
#
#
# @app.route('/', methods=['GET', 'POST'])
# def home():
#     # return '<h1>welcome</h1>'
#
#     return render_template('home.html')
#
#
# @app.route('/signin', methods=['GET'])
# def signin_page():
#     # return '''<form action="/signin" method="post">
#     #              <p><input name="username"></p>
#     #              <p><input name="password" type="password"></p>
#     #              <p><button type="submit">Sign In</button></p>
#     #              </form>'''
#
#     return render_template('form.html')
#
#
# @app.route('/signin', methods=['POST'])
# def signin():
#     # if request.form['username'] == 'admin' and request.form['password'] == 'password':
#     #     return '<h3>Hello, admin!</h3>'
#     # return '<h3>Bad username or password.</h3>'
#
#     username = request.form['username']
#     password = request.form['password']
#     if username == 'admin' and password == 'password':
#         return render_template('signin_ok.html', username=username)
#     return render_template('form.html', message='Bad username or password', username=username)
#
#
# if __name__ == '__main__':
#     app.run()
