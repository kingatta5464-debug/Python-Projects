import math


class Shape:
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        a = math.pi * self.radius * self.radius
        print(f"Area of circle: {a}")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        a = self.length * self.width
        print(f"Area of rectangle: {a}")


# Create objects
s1 = Circle(2)
s2 = Rectangle(2, 2)

# Call methods
s1.calculate_area()
s2.calculate_area()
