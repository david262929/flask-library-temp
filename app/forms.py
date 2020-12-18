# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, DateTimeField, PasswordField)
from wtforms.validators import InputRequired


class ExampleForm(FlaskForm):
    title = StringField('title', validators=[InputRequired()])
    content = TextAreaField('content')
    date = DateTimeField('date', format='%d/%m/%Y %H:%M')


class LoginForm(FlaskForm):
    user = StringField('username', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])
