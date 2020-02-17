#! /bin/bash

source env/bin/activate;
echo ' * Virtual enviroment: Active';
export FLASK_APP=run.py;
export FLASK_DEBUG=True;
echo ' * FLASK_APP: run.py';
echo ' * FLASK_DEBUG: True';
flask run --host=0.0.0.0 --port=5001;