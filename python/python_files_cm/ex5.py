#Author: Gal Elhiani
#Tester: Noam Kux

from pathlib import Path

dir_path = Path(".")

def combine_files(directory_path):
    '''a function to combine all txt files into one'''
    file_list = []
    merged_file = directory_path / "merged.txt"

    for file in directory_path.iterdir():
        if file.suffix == ".txt" and file != merged_file:
            file_list.append(file)
        

    with open(merged_file, "w", encoding="utf-8") as new_merged_file:
        for file_path in file_list:                                     #exclude current file
            if file_path == merged_file:
                continue
            
            with open(file_path, "r", encoding="utf-8") as curr_file:
                new_merged_file.write(curr_file.read() + '\n')


combine_files(dir_path)