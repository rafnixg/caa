# -*- encoding: utf-8 -*-
"""
License: MIT.

Copyright (c) 2019 - present AppSeed.us
"""

from flask import Blueprint

blueprint = Blueprint(
    'register_blueprint',
    __name__,
    url_prefix='/register',
    template_folder='templates',
    static_folder='static',
)
