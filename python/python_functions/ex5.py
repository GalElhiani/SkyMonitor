#5. Write a function that receives a dictionary with names of products and their prices and returns the dictionary with a 10% sale price.
#Author: Gal ELhiani
#Tester: Or Mano


test_dict = {
    "Wireless Mouse": 25,
    "Coffee Mug": 12.5,
    "Leather Jacket": 18,
    "Speaker": 45,
    "Lamp": 32,
    "Shoes": 89,
    "Bottle": 15,
    "Backpack": 49
}


def sale_discount(target_dict):
    '''a function that receives a dictionary with names of products and their prices and returns
    the dictionary with a 10% sale price.'''
    for key in target_dict.keys():
        target_dict[key]*=1.1
    return target_dict


print(sale_discount(test_dict))