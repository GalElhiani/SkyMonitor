#this program demonstrates a function that removes and prints every second number
#from a list of numbers until the list becomes empty.
#Author: Gal Elhiani
#Tester: Tomer

def remove_second(list):
    '''function that removes and prints every second number from a list of numbers until the list becomes empty'''
    while len(list) > 1:
        element = list.pop(1)
        print(element)

    last_element = list.pop()
    print(last_element)
            
    return list




lst = [1, 2, 3, 4, 5, 6, 7, 8]
print(remove_second(lst))


