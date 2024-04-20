#!/usr/bin/python3

import subprocess
import sys
import os 
import datetime

log_file = '/home/lehlomela/Desktop/error.log'

def push_to_remote_repository(folder_name, remote='origin', branch_name='main'): 
    log_error(f'pushing folder {folder_name}')
    try: # check if git repository
        subprocess.check_output(["git", "-C", folder_name, "rev-parse"], stderr=subprocess.DEVNULL)
        auto_commit_changes(folder_name, remote, branch_name)
    except subprocess.CalledProcessError as ex:
        log_error(f'folder {folder_name} not a git repository \n error:', ex)
    
def auto_commit_changes(folder, remote, branch_name): 
    try:
        # os.chdir(folder)
        # subprocess.check_call(['git', 'add', '.'])
        # subprocess.check_call(['git', 'commit', '-m', f'auto commit msg {datetime.date.today()}'])
        subprocess.check_call(['./auto_commit.sh', folder])
    except subprocess.CalledProcessError as e:
        log_error('Error commiting code to remote repo', e)

def log_error(msg, e=''):
    mode = 'a' if os.path.exists(log_file) else  'w'
        
    with open(log_file, mode) as file:
        file.write(f'{msg} {str(e)}\n date: {datetime.date.today()}\n')
    
        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage git_auto_commit <folder-name>")
        sys.exit(1)

    folder = sys.argv[1]
    push_to_remote_repository(folder_name=folder)
