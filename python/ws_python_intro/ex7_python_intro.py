#this program demonstrates how a function recieves a sum of money and divides it into
#the minimum amount of bills and coins
#Author: Gal Elhiani
#Tester: Ron Cohen

def MoneyToCurrency(num):
    '''calculates how many bills in index i can fit inside our number'''

    bills = [200,100,50,20,10,5,2,1]
    amount_of_bills = [0,0,0,0,0,0,0,0]
    for i in range(len(bills)):
        amount_of_bills[i] = num // bills[i]                            
        num %= bills[i]

    # a simple loop to print the result
    for i in range(len(amount_of_bills)):
        if amount_of_bills[i] != 0:
            if i < 3:
                print(f"There are {amount_of_bills[i]} bills of {bills[i]} ")
            else:
                print(f"There are {amount_of_bills[i]} coins of {bills[i]} ")


        
    return amount_of_bills



num1 = 752
print(MoneyToCurrency(num1))


