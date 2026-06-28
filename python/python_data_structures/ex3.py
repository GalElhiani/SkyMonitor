#this program demonstrates a function that receives 2 list s and returns a list containing only the elements that are in both lists
#Author: Gal Elhiani
#Tester: Tomer

def ListIntersection(list1, list2):
    '''function that receives 2 list s and returns a list containing only the elements that are in both lists'''
    new_set = {}
    new_set = set(list1) & set(list2)
    return new_set


lst1 = [1, 2, 3, 4, 5]
lst2 = [5, 6, 7, 8, 9]

print(ListIntersection(lst1, lst2))