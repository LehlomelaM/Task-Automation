#!/usr/bin/python3

import os
import re
import shutil
import sys

main_dir = 'Notes/'

def move_file_to_directory(file_path, file_dir):
    dir_to_paste = f'{main_dir}{file_dir}'

    if not os.path.exists(dir_to_paste):
        os.makedirs(dir_to_paste)
    # move files
    shutil.move(file_path, dir_to_paste)


def search_files_for_tags(dir):
    pattern = re.compile(r'^\s*tags:\s*\[(.*)\]\s*$') # Notable

    for filename in os.listdir(dir):
        
        if os.path.isfile(filename) and filename.endswith('.md'): # select markdown files
            with open(filename, 'r') as file:
                for line in file: 
                
                    match = pattern.match(line)
                    if match:
                        folder_name = match.group(1)
                        move_file_to_directory(filename, folder_name)
                        break
    
    destination_folder = './Notes/images/'
    if(os.path.exists(destination_folder)):
        shutil.rmtree(destination_folder)
    shutil.copytree('./images', destination_folder)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage move_files_to_folders.py <folder-name>")
        sys.exit(1)

    search_files_for_tags(sys.argv[1])
