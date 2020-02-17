# -*- encoding: utf-8 -*-
"""
License: MIT.

Copyright (c) 2019 - present AppSeed.us
"""

from flask import render_template, redirect, request, url_for
from flask_login import (
    current_user,
    login_user,
    logout_user
    # login_required,
)

from app import db, login_manager
from app.base import blueprint
from app.base.forms import LoginForm, CreateAccountForm
from app.base.models import User

from app.base.util import verify_pass


@blueprint.route('/')
def route_default():
    """Route default."""
    return redirect(url_for('base_blueprint.login'))


@blueprint.route('/error-<error>')
def route_errors(error):
    """Route errors."""
    return render_template('errors/{}.html'.format(error))


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    """Route Login."""
    login_form = LoginForm(request.form)
    if 'login' in request.form:
        # read form data
        username = request.form['username']
        password = request.form['password']

        # Locate user
        user = User.query.filter_by(username=username).first()

        # Check the password
        if user and verify_pass(password, user.password):

            login_user(user)
            return redirect(url_for('base_blueprint.route_default'))

        # Something (user or pass) is not ok
        return render_template(
            'login/login.html', msg='Wrong user or password', form=login_form)

    if not current_user.is_authenticated:
        return render_template('login/login.html', form=login_form)
    return redirect(url_for('home_blueprint.index'))


@blueprint.route('/create_user', methods=['GET', 'POST'])
def create_user():
    """Create user route."""
    # login_form = LoginForm(request.form)
    create_account_form = CreateAccountForm(request.form)
    if 'register' in request.form:

        username = request.form['username']
        email = request.form['email']

        user = User.query.filter_by(username=username).first()
        if user:
            return render_template('login/register.html',
                                   msg='Username already registered',
                                   form=create_account_form)

        user = User.query.filter_by(email=email).first()
        if user:
            return render_template('login/register.html',
                                   msg='Email already registered',
                                   form=create_account_form)

        # else we can create the user
        user = User(**request.form)
        db.session.add(user)
        db.session.commit()

        return render_template('login/register.html',
                               msg='User created please <a href="/login">login</a>',  # noqa
                               form=create_account_form)

    else:
        return render_template('login/register.html', form=create_account_form)


@blueprint.route('/logout')
def logout():
    """Logout route."""
    logout_user()
    return redirect(url_for('base_blueprint.login'))


@blueprint.route('/shutdown')
def shutdown():
    """Shutdown route."""
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return 'Server shutting down...'


@login_manager.unauthorized_handler
def unauthorized_handler():
    """Unautorized route."""
    return render_template('errors/403.html'), 403


@blueprint.errorhandler(403)
def access_forbidden(error):
    """Route error 403."""
    return render_template('errors/403.html'), 403


@blueprint.errorhandler(404)
def not_found_error(error):
    """Route Error 404."""
    return render_template('errors/404.html'), 404


@blueprint.errorhandler(500)
def internal_error(error):
    """Route Error 500."""
    return render_template('errors/500.html'), 500
