# -*- encoding: utf-8 -*-
"""
License: MIT.

Copyright (c) 2019 - present AppSeed.us
"""

import os
from dotenv import load_dotenv
load_dotenv()


class Config(object):
    """Config Base."""

    basedir = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = 'key'

    # This will create a file in <app> FOLDER
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')  # noqa

    # For 'in memory' database, please use:
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # THEME SUPPORT
    #  if set then url_for('static', filename='', theme='')
    #  will add the theme name to the static URL:
    #    /static/<DEFAULT_THEME>/filename
    # DEFAULT_THEME = "themes/dark"
    DEFAULT_THEME = None


class ProductionConfig(Config):
    """Poroduction config."""

    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    # PostgreSQL database
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(
        os.getenv('DATABASE_USER', 'caa'),
        os.getenv('DATABASE_PASSWORD', 'caa'),
        os.getenv('DATABASE_HOST', 'db'),
        os.getenv('DATABASE_PORT', 5432),
        os.getenv('DATABASE_NAME', 'caa')
    )


class DebugConfig(Config):
    """Debug Config."""

    DEBUG = True


config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig
}
