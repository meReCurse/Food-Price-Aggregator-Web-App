#!/usr/bin/env bash

project=$(ls -l | grep "^d" | grep -v "dev" | rev | cut -d" " -f1 | rev)

name=admin
pass=$(< /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c 15)
mail=$name@example.com

pipenv run $project/manage.py shell -c "\
from django.contrib.auth import get_user_model;\
User = get_user_model();\
User.objects.create_superuser('$name', '$mail', '$pass')"

echo $pass > dev/pass/$name.pass
