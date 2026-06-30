#Author: Gal Elhiani
#Tester: Or Mano

import os
import sys
import stat

file_name = sys.argv[1]                                    #get file name from CLI
search_dir = "/"                                           #set start point for search

for root, dirs, files in os.walk(search_dir):              #use os.walk to iterate over the system
    if file_name in files:
        full_path = os.path.join(root, file_name)          #get the full path of the file
        print(f"File found at: {full_path}")
        break                                              #stops the script after finding the first match
else:
    print("File not found")

if os.access(full_path, os.X_OK):                          #check permissions using full path
    print("file has execution permissions")
else:                                                      #if not execute permissions, set them for owner and group
    current_mode = os.stat(full_path).st_mode
    os.chmod(full_path, current_mode | stat.S_IXUSR | stat.S_IXGRP)
    print("Changed permissions successfully")