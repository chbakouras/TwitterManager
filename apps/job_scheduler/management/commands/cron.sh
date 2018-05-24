#!/bin/bash

PATH=$1
MANAGE_PATH=$PATH/manage.py
COMMAND="pipenv run python3.5 $MANAGE_PATH scheduler"
cd $PATH

(/usr/bin/sleep 5 && eval $COMMAND) &
(/usr/bin/sleep 10 && eval $COMMAND) &
(/usr/bin/sleep 15 && eval $COMMAND) &
(/usr/bin/sleep 20 && eval $COMMAND) &
(/usr/bin/sleep 25 && eval $COMMAND) &
(/usr/bin/sleep 30 && eval $COMMAND) &
(/usr/bin/sleep 35 && eval $COMMAND) &
(/usr/bin/sleep 40 && eval $COMMAND) &
(/usr/bin/sleep 45 && eval $COMMAND) &
(/usr/bin/sleep 50 && eval $COMMAND) &
(/usr/bin/sleep 55 && eval $COMMAND) &
