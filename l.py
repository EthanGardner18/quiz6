# To fix the violation, just add it into the class

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod

    def get_area():
        print("base class area")

class setWidth(ABC):
    @abstractmethod

    def set_width(self,width):
        self.width = width

class setHeight(ABC):
    @abstractmethod

    def set_height(self,height):
        self.height = height

class Circle(Shape, setWidth):
    
    def __init__(self,radius):
        self.radius = radius

    # the width in this case can just be altered for the radius
    def set_width(self,radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius * self.radius

class Rectangle(Shape, setWidth, setHeight):
   
    def __init__(self,width, height):
        self.width = width
        self.height = height

    def set_width(self,width):
        self.width = width

    def set_height(self,height):
        self.height = height

    def get_area(self):
        return self.width * self.height

class Triangle(Shape, setWidth, setHeight):
   
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def set_width(self,width):
        self.width = width

    def set_height(self,height):
        self.height = height

    def get_area(self):
        return self.height * self.width * 0.5

def main():
    circle = Circle(5)
    rectangle = Rectangle(3, 6)
    triangle = Triangle(4, 5)

    shapes = [circle, rectangle, triangle]

    for shape in shapes:
        print(f"Area of {type(shape).__name__}: {shape.get_area()}")

if __name__ == "__main__":
    main()
