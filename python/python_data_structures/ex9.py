#this program demonstrates a function that, when given two strings,
#returns the first string but without any characters that exist in the second string
#For example f('lorem ipsum', "Imnop') should return re isu.
#Author: Gal Elhiani
#Tester: Tomer

def intersection_strings(string1, string2):
    '''a function that takes two strings and returns the first string without any chars in the second'''
    result = []

    for i in string1:
        if i not in string2:
            result.append(i)
    return result



string_test1 = "hallol"
string_test2 = "hello"

print(intersection_strings(string_test1, string_test2))
