#this program demonstrates how a function that receives a str and returns a dict containing each letter and its occurrence
#Author: Gal Elhiani
#Tester: Tomer

def StrToDictB(string):
    '''a function that receives a str and returns a dict containing each letter and its occurrence.'''
    dictionary = {}
    for i, ch in enumerate(string):
        dictionary[ch] = dictionary.get(ch, 0) + 1

    return dictionary



strong = "testing string"
print(StrToDictB(strong))
