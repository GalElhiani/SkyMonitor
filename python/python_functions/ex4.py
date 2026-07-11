#4. Using list comprehension, construct a list from the squares of each even element in the given list.
#Author: Gal ELhiani
#Tester: Or Mano

lst = [-8, 3, -1, 10, -5, 2, -10, 7, -4, 6]
even_squared = lambda target_list: [num*num for num in target_list if num % 2 == 0]
print(even_squared(lst))