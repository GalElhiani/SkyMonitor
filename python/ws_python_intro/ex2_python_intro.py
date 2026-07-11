#this program demonstrates how a function recieves a number and outputs the reversed number
#Author: Gal Elhiani
#Tester: Ron Cohen

def NumReverser(num):
    '''This function reverses a given number mathematically'''
    abs_num = abs(num)
    reveresed = 0
    prev = 0
    while abs_num > 0:
        prev = abs_num % 10
        reveresed = reveresed + prev
        abs_num = abs_num // 10
        reveresed *= 10
    if num < 0:
        return -(reveresed // 10)
    return reveresed // 10


number = -9832
string = "25.167"
num_float = 12.3

print(NumReverser(number))

def NumReverserAdv(var):
    '''This function reverses a given number and can handle ints, floats and strings'''

    if type(var) == int:
        return str(var)[::-1]
    if type(var) == float:
        return str(var)[::-1]
    if type(var) == str:
        return var[::-1]


print(NumReverserAdv(string))
print(NumReverserAdv(num_float))