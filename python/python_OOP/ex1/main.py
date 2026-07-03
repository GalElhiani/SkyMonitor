#This is a main module to test point.py
#Author: Gal ELhiani
#Tester: Meytar

import point

p1 = point.Point(3, 4)
p2 = point.Point(14, 20)
p3 = point.Point(10, 100)

print(p1.distance_from_origin())
print(p2.distance_from_origin())
print(p3.distance_from_origin())