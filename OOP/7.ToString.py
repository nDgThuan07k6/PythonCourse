class Person:
    def __init__(self, name, age    ):
        self.name = name
        self.age = age
    
    def print_info(self):
        return f'{self.name} is {self.age} years old'

    # Magic method: Using __str__ in order to convert and print string without calling function
    def __str__(self):
        return f'{self.name} is {self.age} years old'

person1 = Person('Kiet', 19)
person2 = Person('Thuan', 19)
print(person1)
print(person2.print_info())
print(person2)