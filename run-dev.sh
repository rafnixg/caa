#! /bin/bash

source env/bin/activate;
echo ' * Virtual enviroment: Active';
export FLASK_APP=run.py;
export FLASK_ENV=development;
flask run --host=0.0.0.0 --port=5001;