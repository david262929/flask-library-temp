# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

import os
from flask import render_template, Response # url_for, redirect, render_template, flash, g
# from flask_login import login_user, logout_user, current_user, login_required

# from app.forms import (ExampleForm, LoginForm)
from app import app # , lm
# from app.models import User

@app.errorhandler(Exception)
def handle_bad_request(e):
    return 'bad request!', 404

@app.route('/')
def index():
	return render_template("index.html", flask_token='token-token-_-token-token')

# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def get_resource(path):  # pragma: no cover
#     mimetypes = {
#         ".css": "text/css",
#         ".html": "text/html",
#         ".js": "application/javascript",
#     }
#     complete_path = os.path.join(root_dir(), path)
#     ext = os.path.splitext(path)[1]
#     mimetype = mimetypes.get(ext, "text/html")
#     content = get_file(complete_path)
#     return Response(content, mimetype=mimetype)



# @app.route('/list/')
# def posts():
# 	return render_template('list.html')
#
# @app.route('/new/')
# @login_required
# def new():
# 	form = ExampleForm()
# 	return render_template('new.html', form=form)
#
# @app.route('/save/', methods = ['GET','POST'])
# @login_required
# def save():
# 	form = ExampleForm()
# 	if form.validate_on_submit():
# 		print("salvando os dados:")
# 		print(form.title.data)
# 		print(form.content.data)
# 		print(form.date.data)
# 		flash('Dados salvos!')
# 	return render_template('new.html', form=form)
#
# @app.route('/view/<id>/')
# def view(id):
# 	return render_template('view.html')
#
# # === User login methods ===
#
# @app.before_request
# def before_request():
#     g.user = current_user
#
# @lm.user_loader
# def load_user(id):
#     return User.query.get(int(id))
#
# @app.route('/login/', methods = ['GET', 'POST'])
# def login():
#     if g.user is not None and g.user.is_authenticated():
#         return redirect(url_for('index'))
#     form = LoginForm()
#     if form.validate_on_submit():
#         login_user(g.user)
#
#     return render_template('login.html',
#         title = 'Sign In',
#         form = form)
#
# @app.route('/logout/')
# def logout():
#     logout_user()
#     return redirect(url_for('index'))

# ====================