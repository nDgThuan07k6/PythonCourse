import math

class Circle:
    def __init__(self, radius):
        # Radius is private
        self._radius = radius

    # Using property to call a function without ()
    @property
    def radius(self):
        return self._radius
    
    # Using radius.setter in order to set a new value without error
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be greater than 0")
        self._radius = value

    @property
    def area(self):
        return math.pi * (self._radius ** 2)
    
c = Circle(5)
print('Radius of circle:', c.radius)
print('Area of circle:', c.area)

c = Circle(10)
print('Radius of circle:', c.radius)
print('Area of circle:', c.area)