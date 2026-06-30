#3. Write a program to calculate the sum of the positive and negative numbers of a given list of numbers using lambda function.
#Author: Gal ELhiani
#Tester: Or Mano

lst = [-42, 87, -5, 12, -93, 0, 56, -18, 71, -3]
positive_sum = lambda target_list: sum(filter(lambda x: x > 0, target_list))
negative_sum = lambda target_list: sum(filter(lambda x: x < 0, target_list))


print(positive_sum(lst))
print(negative_sum(lst))
