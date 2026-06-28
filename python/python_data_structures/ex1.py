#this program demonstrates a function that recieves a list and returns the list without non-str types
#Author: Gal Elhiani
#Tester: Tomer

def RemoveNonStr(list):
    '''This function recieves a list and removes all non str objects from'''
    lst[:] = [obj for obj in list if isinstance(obj, str)]  #replace the entire contents of the list



lst = ["hello", "my", 2.5, "name ", 15,"is", "gal"]
RemoveNonStr(lst)
print(lst)

