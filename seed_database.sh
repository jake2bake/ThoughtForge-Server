#!/bin/bash

rm db.sqlite3
rm -rf ./thoughtsapi/migrations
python3 manage.py makemigrations thoughtsapi
python3 manage.py migrate
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata topics.json
python3 manage.py loaddata courses.json
python3 manage.py loaddata readings.json
python3 manage.py loaddata tags.json
python3 manage.py loaddata entries.json
python3 manage.py loaddata entryTags.json
python3 manage.py loaddata courseEnrollments.json
python3 manage.py loaddata readingAssignments.json
python3 manage.py loaddata submissions.json
python3 manage.py loaddata shares.json
python3 manage.py loaddata likes.json