#!/bin/bash

pipenv shell

MANAGE_PATH=$1
COMMAND="python3.5 $MANAGE_PATH scheduler"

(sleep 5 && eval $COMMAND) &
(sleep 10 && eval $COMMAND) &
(sleep 15 && eval $COMMAND) &
(sleep 20 && eval $COMMAND) &
(sleep 25 && eval $COMMAND) &
(sleep 30 && eval $COMMAND) &
(sleep 35 && eval $COMMAND) &
(sleep 40 && eval $COMMAND) &
(sleep 45 && eval $COMMAND) &
(sleep 50 && eval $COMMAND) &
(sleep 55 && eval $COMMAND) &
