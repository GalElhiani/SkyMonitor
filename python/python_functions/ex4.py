lst = [-8, 3, -1, 10, -5, 2, -10, 7, -4, 6]
even_squared = lambda target_list: [num*num for num in target_list if num % 2 == 0]
print(even_squared(lst))