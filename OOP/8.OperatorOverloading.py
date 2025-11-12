class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Call __add__ when vector1 + vector2
    # self: vector1 || other: vector2
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f'{self.x}, {self.y}'
    
vector1 = Vector2D(3, 2)
vector2 = Vector2D(2, 1)
vector3 = vector1 + vector2
print(f'Sum of two vectors: ({vector3})')
