#Write your module "areas" with 3 functions:
#Circle area - A function that takes a radius of a circle and returns its area.
#Triangle area -A function that takes the height and width of a triangle and returns its area.
#Rectangle area - A function that takes the width and height of a rectangle and returns its area.


#Author: Gal Elhiani
#Tester: Or Mano

from math import pi

def circle_area(radius):
    '''function to calculate the area of a circle given a radius'''
    return (radius**2)*pi

def triangle_area(height, width):
    '''function to calculate the area of a triangle given height and width'''
    return (height*width)/2

def rectangle_area(height, width):
    '''function to calculate the area of a rectangle given height and width'''
    return height*width