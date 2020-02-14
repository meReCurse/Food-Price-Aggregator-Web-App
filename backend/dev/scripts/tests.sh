#!/usr/bin/env bash

project=$(ls -l | grep "^d" | grep -v "dev" | rev | cut -d" " -f1 | rev)

for x in $(ls -d $project/apps/*/); do
    f="$(basename $x)"
    pipenv run python $project/manage.py test $project/apps/$f
done
