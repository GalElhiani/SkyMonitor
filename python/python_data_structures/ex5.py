#this program demonstrates a function that receives a list and performs a left rotation using slicing.
#Author: Gal Elhiani
#Tester: Tomer

def left_rotation(list):
    '''a function that receives a list and performs a left rotation using slicing'''
    return list[1::] + list[:1:]


lst = [1, 2, 3, 4, 5]
print(left_rotation(lst))