#!/usr/bin/env bash

project=$(ls -l | grep "^d" | grep -v "dev" | rev | cut -d" " -f1 | rev)

pipenv run python $project/manage.py shell <<EOF
from django.test.utils import setup_test_environment
from django.test import Client
from django.urls import reverse


setup_test_environment()
client = Client()
response = client.get(reverse('polls:index'))
response_dict = {
    "status": response.status_code,
    "content": response.content,
    "context": response.context
}

for k, v in response_dict.items():
    print(f'{k:#^30}')
    if k == "context":
        i = 0
        for el in v:
            print(f'{i}:\n{"":>4}{el}')
            i += 1
    else:
        print(f'{v}\n')

EOF
