#Author: Gal Elhiani
#Tester: Noam Kux

import csv
from pathlib import Path

file_path = Path("corona.csv")

with open(file_path, "r", encoding="utf-8") as file:
    csv_reader = list(csv.reader(file))


    headers = csv_reader[0]
    age_list = []
    hospitalization_list = []
    result = 0
    age_index = headers.index("Age")
    hospitalization_index = headers.index("Length_of_hospitalization")

    for index, row in enumerate(csv_reader):
        #go past headers
        if index == 0:
            continue

        age_list.append(int(row[age_index]))
        hospitalization_list.append(int(row[hospitalization_index]))

    for i in hospitalization_list:
        result+= i
    
    hospitalization_mean = result / len(hospitalization_list)

    print(headers)

    print("max age", max(age_list))
    print("min age", min(age_list))
    
    print(hospitalization_mean)


def filter_file(data_source, target_cols, output_file):
    '''a function that filters out specific data colunms requested by the user'''
    headers = data_source[0]
    target_index_list = []
    for col in target_cols:
        if col in headers:
            target_index_list.append(headers.index(col))


    with open(output_file, "w", encoding="utf-8") as file:
        for row in data_source:
            filtered = []
            for i in target_index_list:
                filtered.append(row[i])
            
            #format according to csv
            new_line = ",".join(filtered)
            file.write(new_line + "\n")


target_list = ["gender", "Age", "Is_vaccinated"]
filter_file(csv_reader, target_list, "Test.csv")

