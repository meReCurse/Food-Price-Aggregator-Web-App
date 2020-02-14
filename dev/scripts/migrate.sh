#!/usr/bin/env bash

project=$(ls -l | grep "^d" | grep -v "dev" | rev | cut -d" " -f1 | rev)

pipenv run python $project/manage.py makemigrations
pipenv run python $project/manage.py migrate
