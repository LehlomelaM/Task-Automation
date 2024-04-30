#!/bin/bash
echo -e "\n\nRunning daily tasks $(date)"

SCRIPTS_HOME='/home/lehlomela/Documents/bin/'
NOTES='/home/lehlomela/Documents/notes'

cd $SCRIPTS_HOME

# back up scripts
auto_commit.sh .

# moves Notable markdown files to folders based on tags
move_files_to_folders.py $NOTES
# auto_commit.sh $NOTES/Notes/