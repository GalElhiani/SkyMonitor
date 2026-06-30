#Create a function that checks if a given name is defined in the global namespace.
#Author: Gal Elhiani
#Tester: Or Mano
test = 1

def is_in_global(name):
    '''a function that checks if a given name is defined in the global namespace'''
    return name in globals()


print(is_in_global("test"))