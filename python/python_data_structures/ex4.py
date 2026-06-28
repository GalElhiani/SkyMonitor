#this program demonstrates a function that receives a dictionary 
#and returns list with all unique values in a given dictionary.
#Author: Gal Elhiani
#Tester: Tomer

def unique_vals(dictionary):
    '''a function that receives a dictionary and returns list with all unique values in a given dictionary'''
    lst = set(dictionary.values())
    return list(lst)


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
print(unique_vals(simple_dict))