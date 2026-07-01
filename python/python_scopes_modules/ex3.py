#write a program that prints the operating system name, 
#the name of the logged user, and the current working directory.

#Author: Gal Elhiani
#Tester: Or Mano

import os

print(os.name)
print(os.getlogin())
print(os.getcwd())