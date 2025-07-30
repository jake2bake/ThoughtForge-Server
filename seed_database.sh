#!/bin/bash

rm db.sqlite3
rm -rf ./thoughtsapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations thoughtsapi
python3 manage.py migrate thoughtsapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens

