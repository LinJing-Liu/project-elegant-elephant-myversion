#!/bin/bash

python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
export FLASK_ENV=development
flask run