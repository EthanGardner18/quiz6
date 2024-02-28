import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area():
        print("area")

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius * self.radius 

class Square(Shape):

    def __init__(self,side):
        self.side = side

    def get_area(self):
        return self.side * self.side
class Rectangle(Shape):

    def __init__(self,length,height):
        self.length = length
        self.height = height
    
    def get_area(self):
        return self.length * self.height
    
class Triangle(Shape):
    
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height
    

def main():
    circle = Circle(5)
    square = Square(4)
    rectangle = Rectangle(3, 6)
    triangle = Triangle(4, 5)

    shapes = [circle, square, rectangle, triangle]

    for shape in shapes:
        print(f"Area of {type(shape).__name__}: {shape.get_area()}")


if __name__ == "__main__":
    main()
