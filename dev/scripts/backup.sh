#!/usr/bin/env bash

project=$(ls -l | grep "^d" | grep -v "dev" | rev | cut -d" " -f1 | rev)

tar cvzf dev/bak/$project$(date +'%s').tar.gz $project
