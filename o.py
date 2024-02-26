import math


class Shape:
    
    def __init__(self) -> None:
        pass
    
    def get_area():
        pass

class Circle():

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius * self.radius 

class Square():

    def __init__(self,side):
        self.side = side

    def get_area(self):
        return self.side * self.side
class Rectange():

    def __init__(self,length,height):
        self.length = length
        self.height = height
    
    def get_area(self):
        return self.length * self.height
    
class Triangle():
    
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height
