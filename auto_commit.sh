#!/bin/bash

DATE=date

if [ "$#" -eq 1 ]; then
    cd $1
    pwd >> ~/Desktop/directory.file
    # commit local changes
    git add .
    git commit -m "auto commit message $DATE"
    git push origin main
    echo 'managed to push to origin' $1 >> ~/Desktop/testing.file
fi