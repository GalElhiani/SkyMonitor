from math import sqrt

class Point:
    def __init__(self, x=0.0, y=0.0):
        if not isinstance(x, (float, int)) or not isinstance(y, (float, int)):
            raise ValueError("x and y must be a number!")
        self.x = x
        self.y = y
    def distance_from_origin(self, point):
        return sqrt((point.x - self.x)**2 + (point.y - self.y)**2)

