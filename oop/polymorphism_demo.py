import math
# Base class - Shape
class Shape:
    def area(self):
        # Force subclasses to implement this method
        raise NotImplementedError("Subclasses must implement the area method")

# Derived class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Derived class - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
