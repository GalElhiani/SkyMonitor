#this program demonstrates how a function takes a number and checks if its prime
#Author: Gal Elhiani
#Tester: Ron Cohen

def IsPrime(num):
    '''Function to check if a number is prime'''
    if num < 2:                 # 1,2 are prime numbers and cant be included
        return False
    i = 2
    while i*i <= num:            # the biggest sum a number can be divided to is its square root (to get an int)
        if num % i == 0:
            return False
        i+=1
    return True
        



num = 15
num2 = 180
num3 = 7
num4 = 3
print(IsPrime(num))
print(IsPrime(num2))
print(IsPrime(num3))
print(IsPrime(num4))
