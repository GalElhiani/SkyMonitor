#this program demonstrates how a function recieves a number and then calculates the sum
#of its divisors
#Author: Gal Elhiani
#Tester: Ron Cohen

def SumOfDivisors(num):
    '''function that calculates the sum of divisors of a given number'''
    if num < 0:
        return 0
    if num == 0:
        return 0
    
    result = 0
    for i in range(1 , num+1):
        if num % i == 0:
            result += i
    return result 






num1 = -100
num2  = 150
num3 = 12
num4 = 7

print(SumOfDivisors(num1))
print(SumOfDivisors(num2))
print(SumOfDivisors(num3))
print(SumOfDivisors(num4))