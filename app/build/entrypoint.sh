#!/bin/sh
cd /home/app

python migrations.py db init
python migrations.py db migrate
python migrations.py db upgrade
python app.py
