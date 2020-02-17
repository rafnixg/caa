# -*- encoding: utf-8 -*-
"""
License: MIT.

Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField
from wtforms.validators import InputRequired, Email, DataRequired  # noqa

# login and registration


class LoginForm(FlaskForm):
    """Login form."""

    username = TextField('Username', id='username_login', validators=[DataRequired()])  # noqa
    password = PasswordField('Password', id='pwd_login', validators=[DataRequired()])  # noqa


class CreateAccountForm(FlaskForm):
    """Registration form."""

    username = TextField('Username', id='username_create', validators=[DataRequired()])  # noqa
    email = TextField('Email', id='email_create', validators=[DataRequired(), Email()])  # noqa
    password = PasswordField('Password', id='pwd_create', validators=[DataRequired()])  # noqa
