#!/bin/bash

DATE=date

if [ "$#" -eq 1 ]; then
    cd $1

    # commit local changes
    git add .
    git commit -m "auto commit message $DATE"
    git push origin main
fi