#Author: Gal Elhiani
#Tester: Noam Kux


import csv
import json
from pathlib import Path

def convert_to_json(file_path, file_dest):
    '''takes file csv file_path and converts it into a json file in file_dest path'''
    src = Path(file_path)
    dest = Path(file_dest)
    with open(src, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        data = list(reader)


    with open(dest, "w", encoding="utf-8") as json_file:
       json.dump(data, json_file, indent=4)


path = Path("corona.csv")
convert_to_json(path, "new_json")