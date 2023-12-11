#!/bin/bash
# bash script that takes URL ,post and diplay body: set email and subject
curl -sX POST -d "email:test@gmail.com" "subject:I will always be here for PLD" "$1"
