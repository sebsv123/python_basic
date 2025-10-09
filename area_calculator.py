import math
import os
class Rectangle:
    def __init__(self, length, height):
        self.length = length
        self.height = height

    def area(self):
        return round(self.length * self.height, 2)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * (self.radius ** 2), 2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())

    for _ in range(q):
        args = input().split()
        shape_name, params = args[0], tuple(map(int, args[1:]))

        if shape_name == "rectangle":
            a, b = params
            shape = Rectangle(a, b)
        elif shape_name == "circle":
            r = params[0]
            shape = Circle(r)
        else:
            raise ValueError("Invalid shape type")

        fptr.write("%.2f\n" % shape.area())

    fptr.close()

