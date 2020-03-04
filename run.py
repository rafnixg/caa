# -*- encoding: utf-8 -*-
"""
License: MIT.

Copyright (c) 2019 - present AppSeed.us
"""

from flask_migrate import Migrate
from sys import exit
import os

from config import config_dict
from app import create_app, db

get_config_mode = os.getenv('CONFIG_MODE', 'Debug')

try:
    config_mode = config_dict[get_config_mode.capitalize()]
except KeyError:
    exit('Error: Invalid CONFIG_MODE environment variable entry.')

app = create_app(config_mode)
Migrate(app, db)
