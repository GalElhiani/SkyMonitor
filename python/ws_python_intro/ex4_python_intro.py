#this program demonstrates how a function recieves a year and checks if its a leap year
#Author: Gal Elhiani
#Tester: Ron Cohen

def IsLeapYear(num):
    '''This function calculates if a given year is a leap year'''
    if (num % 4 == 0 and num % 100 != 0) or (num % 400 == 0):
        return True
    return False



year = 2020
print(IsLeapYear(year))