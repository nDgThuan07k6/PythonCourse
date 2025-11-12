# Base class
import math

class Shape:
    def area(self):
        raise NotImplementedError('Subclass must implement area()')

# Override basic class with circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * math.pi

#Override basic class with rectangle class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
circle1 = Circle(4)
rec1 = Rectangle(2, 4)
print(f'Area of the circle: {math.ceil(circle1.area())}')
print(f'Area of the rectangle: {rec1.area()}')