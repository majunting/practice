from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'user1'}
	posts = [
		{
			'author': {'username': 'user2'},
			'body': 'Post 1'
		},
		{
			'author': {'username': 'user3'},
			'body': 'Post2'
		}
	]
	return render_template('index.html', title = 'home', user = user, posts = posts)
# 	return '''
# <html>
#     <head>
#         <title>Home Page - Microblog</title>
#     </head>
#     <body>
#         <h1>Hello, ''' + user['username'] + '''!</h1>
#     </body>
# </html>'''

@app.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me = {}'.format(
			form.username.data, form.remember_me.data))
		return redirect('/index')
	return render_template('login.html', title = 'Sign In', form = form)