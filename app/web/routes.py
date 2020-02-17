# -*- encoding: utf-8 -*-
"""
License: MIT.

Copyright (c) 2019 - present AppSeed.us
"""

from app.web import blueprint
from flask import render_template  # redirect, url_for
from flask_login import login_required  # current_user
# from app import login_manager
# from jinja2 import TemplateNotFound


@blueprint.route('/')
@login_required
def index():
    """Index page."""
    data = {
        'title': '6to Foro latinoamericano',
    }

    return render_template('index.html', **data)


# @blueprint.route('/<template>')
# def route_template(template):
#     """Template route's."""
#     if not current_user.is_authenticated:
#         return redirect(url_for('base_blueprint.login'))

#     try:
#         return render_template(template + '.html')
#     except TemplateNotFound:
#         return render_template('page-404.html'), 404
#     except:
#         return render_template('page-500.html'), 500
