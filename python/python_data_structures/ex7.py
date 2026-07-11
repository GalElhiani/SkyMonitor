#this program demonstrates a function to convert a given dictionary to a list of tuples.
#Author: Gal Elhiani
#Tester: Tomer
def dict_to_list(dictionary):
    '''a function to convert a given dictionary to a list of tuples.'''
    return list(dictionary.items())

simple_dict = {
    1: "a",
    2: "a",
    3: "a",
    4: "d",
    5: "e",
    6: "f",
    7: "g",
    8: "h",
    9: "i",
    10: "j"
}

print(dict_to_list(simple_dict))