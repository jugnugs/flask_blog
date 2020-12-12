from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
  user = {'username': 'jugnugs'}
  posts = [
    {
      'author': {'username': 'John'},
      'body': 'さようなら'
    },
    {
      'author': {'username': 'Macy'},
      'body': 'あの。。。どこ？'
    }
  ]
  return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')
def login():
  form = LoginForm()
  return render_template('login.html', title='Sign In', form=form)