#!/bin/bash

MANAGE_PATH=$1
COMMAND="python3.5 $MANAGE_PATH scheduler"

(sleep 5 && $COMMAND) &
(sleep 10 && $COMMAND) &
(sleep 15 && $COMMAND) &
(sleep 20 && $COMMAND) &
(sleep 25 && $COMMAND) &
(sleep 30 && $COMMAND) &
(sleep 35 && $COMMAND) &
(sleep 40 && $COMMAND) &
(sleep 45 && $COMMAND) &
(sleep 50 && $COMMAND) &
(sleep 55 && $COMMAND) &
