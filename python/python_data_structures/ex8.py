#this program demonstrates a function to find the maximum and the minimum values in a
#dictionary and print their keys.
#Author: Gal Elhiani
#Tester: Tomer


def max_min_vals(dictionary):
    '''a function to find the maximum and minimum values in a dictionary and prints their keys'''
    maximum_key = list(dictionary.keys())[0]
    minimum_key = list(dictionary.keys())[0]
    for i, obj in dictionary.items():
        if obj > dictionary[maximum_key]:
            maximum_key = i
        if obj < dictionary[minimum_key]:
            minimum_key = i

    print(maximum_key, minimum_key)   



simple_dict = {
    1: 20,
    2: 10,
    3: 9,
    4: 0,
    5: 29,
    6: 1,
    7: 9,
    8: 7,
    9: 2,
    10: 3
}

max_min_vals(simple_dict)