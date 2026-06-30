from functools import reduce

def luhn_algorithm(string):
    lst = [int(ch) for ch in string]
    lst.reverse()
    lst = [num * 2 if index % 2 != 0 else num for index, num in enumerate(lst)]
    lst = list(map(lambda x: x-9 if x > 9 else x, lst))
    sum_of_digits = reduce(lambda x, y: x + y, lst, 0)
    if sum_of_digits % 10 == 0:
        return True
    return False

string = "12345"
string2 = "4242424242424242"

print(luhn_algorithm(string))
print(luhn_algorithm(string2))