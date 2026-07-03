#This is point.py module that implements a class point with a function to calculate distance
#Author: Gal ELhiani
#Tester: Meytar

from math import sqrt

class Point:
    '''a class representing a point'''
    def __init__(self, x=0.0, y=0.0):
        '''initializes a point instance'''
        if not isinstance(x, (float, int)) or not isinstance(y, (float, int)):
            raise ValueError("x and y must be a number!")
        self.x = x
        self.y = y
    def distance_from_origin(self):
        '''a method to calculate the distance from point of origin'''
        return sqrt(self.x**2 + self.y**2)
