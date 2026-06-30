#1. Write a program to remove specific words from a given list using lambda.
#2. Write a program to sort a list of strings(numbers) numerically. Use lambda.
#3. Write a program to calculate the sum of the positive and negative numbers of a given list of numbers using lambda function.
#4. Using list comprehension, construct a list from the squares of each even element in the given list.
#5. Write a function that receives a dictionary with names of products and their prices and returns the dictionary with a 10% sale price.
#6. Gematria is the practice of assigning a numerical value to a name, word, or phrase according to an alphanumerical cipher.
#Write a program that returns the value of the Hebrew phrase/word.
#You can use the Gematria table on the Wiki: https://en.wikipedia.org/wiki/Gematria
#Examples:
#936 = "ni7u"
#7. Implement the Luhn algorithm for the validation of credit card numbers.
#Description of algorithm:
#• The first step of the Luhn algorithm is to double every second digit, starting from the right.
#• If doubling the number results in a number greater than 9, subtract 9 from the product.
#• Then take the sum of all the digits.
#• If the sum is evenly divisible by 10, then the number is valid.



def remove_given_string(string, input_list):
    '''function to remove specific words from a given list using lambda'''
    return list(filter(lambda target: target != string, input_list))





result = lambda string, input_list: list(filter(lambda target: target != string, input_list))
'''lambda function to remove specific words from a given list'''

test_string = "name"
lst = ["my", "name", "is", "slim", "shady"]

print(remove_given_string(test_string, lst))
print(result("shady", lst))