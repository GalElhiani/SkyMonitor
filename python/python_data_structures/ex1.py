#this program demonstrates a function that recieves a list and returns the list without non-str types
#Author: Gal Elhiani
#Tester: Tomer

def remove_non_str(list):
    '''This function recieves a list and removes all non str objects from'''
    lst[:] = [obj for obj in list if isinstance(obj, str)]  #replace the entire contents of the list


lst = ["hello", "my", 2.5, "name ", 15,"is", "gal"]
lst2 = ["hello", "my", 2.5, "name ", 15,"is", "gal"]

remove_non_str(lst)
print(lst)
remove_non_str(lst2)
print(lst2)