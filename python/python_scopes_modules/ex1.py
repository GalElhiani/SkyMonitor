# Create a function that checks if a given name is defined in the global namespace.
# Write your module "areas" with 3 functions:
# • Circle area - A function that takes a radius of a circle and returns its area.
# • Triangle area -A function that takes the height and width of a triangle and returns its area.
# • Rectangle area - A function that takes the width and height of a rectangle and returns its area.
# Import it to the main, call the functions, and print the results.
# Write a program that prints the operating system name, the name of the logged user, and the current working directory.
# Write a program that receives command-line arguments and prints them in reverse order.
# Write a script that takes the file name from the command line, searches for it in the system, 
# and checks the executable permission. If it's missing - change it for the owner and group but not 
# for others.

#Author: Gal Elhiani
#Tester: Or Mano
test = 1

def is_in_global(name):
    '''a function that checks if a given name is defined in the global namespace'''
    return name in globals()


print(is_in_global("test"))