# -*- encoding: utf-8 -*-
"""
License: MIT.

Copyright (c) 2019 - present AppSeed.us
"""

from app.web import blueprint
from flask import render_template  # redirect, url_for
# from flask_login import login_required  # current_user
# from app import login_manager
# from jinja2 import TemplateNotFound

# Import data demo
from app.web.demo import (
    sponsor_types_demo,
    sponsors_demo,
    schedules_demo,
    expositors_demo,
    inversion_demo
)


@blueprint.route('/')
def index():
    """Index page."""
    data = {
        'title': '6to Foro latinoamericano',
        'sponsorTypes': sponsor_types_demo(),
        'sponsors': sponsors_demo(),
        'schedules': schedules_demo(),
        'expositors': expositors_demo(),
        'inversion': inversion_demo(),
        'is_schedules': False,
        'is_counter': False,
    }

    return render_template('web/index.html', **data)


@blueprint.route('/expositors')
def expositors():
    """Expositor views."""
    data = {
        'expositors': expositors_demo()
    }
    return render_template('web/expositors.html', **data)


@blueprint.route('/contact')
def contact():
    """Contact view."""
    return render_template('web/contact.html')


@blueprint.route('/schedule')
def schedule():
    """Schedule view."""
    data = {
        'schedule': schedules_demo()
    }
    return render_template('web/schedule.html', **data)


@blueprint.route('/stay')
def stay():
    """Stay view."""
    return render_template('web/stay.html')


@blueprint.route('/papers')
def papers():
    """Paper view."""
    return render_template('web/papers.html')
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
