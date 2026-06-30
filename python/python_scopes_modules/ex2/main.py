#Import it to the main, call the functions, and print the results.

#Author: Gal Elhiani
#Tester: Or Mano

import areas

def main():
    '''Main function for testing'''
    height = 5
    width = 10
    radius = 2

    print(areas.circle_area(radius))
    print(areas.triangle_area(height, width))
    print(areas.rectangle_area(height, width))

if __name__ == "__main__":
    main()
