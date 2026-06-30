#1. Write a program to remove specific words from a given list using lambda.
#Author: Gal ELhiani
#Tester: Or Mano

result = lambda string, input_list: list(filter(lambda target: target != string, input_list))
'''lambda function to remove specific words from a given list'''

test_string = "name"
lst = ["my", "name", "is", "slim", "shady"]

print(result("shady", lst))