#!/bin/bash
 
SCRIPTS_HOME='/home/lehlomela/Documents/bin/'
NOTES='/home/lehlomela/Documents/notes'

cd $SCRIPTS_HOME

# back up scripts
./auto_commit.sh .

cd $NOTES

# run python script
./move_files_to_folders.py # moves Notable markdown files to folders based on tags
cd $SCRIPTS_HOME
./git_auto_commit.py $NOTES/Notes/ # auto commit recent changes


