#!/usr/bin/env bash

umask 007

project='price_aggregator'
app='rest_api'

mkdir -p dev/{pass,bak,scripts}
mkdir -p $project/apps/$app
touch $project/apps/__init__.py

pipenv --python 3.8
pipenv install django
pipenv install djangorestframework

pipenv run django-admin startproject conf $project/.
pipenv run django-admin startapp $app $project/apps/$app

pipenv run python $project/manage.py migrate

name=admin
pass=$(< /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c 15)
mail=$name@example.com

pipenv run $project/manage.py shell -c "\
from django.contrib.auth import get_user_model;\
User = get_user_model();\
User.objects.create_superuser('$name', '$mail', '$pass')"

echo $pass > dev/pass/admin.pass

pipenv run pip install -r dev/requirements.txt
