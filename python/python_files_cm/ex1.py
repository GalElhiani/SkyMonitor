#Author: Gal Elhiani
#Tester: Noam Kux

import string

lst = list(string.ascii_lowercase)          # list to hold all the alphabet characters as single items

for i in lst:
    with open(f"{i}.txt", "w") as file:
        file.write(i)