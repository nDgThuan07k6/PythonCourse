class Student:
    def __init__(self, name, grade = 0):
        self.name = name
        # Private value include __ (For example: self.__name)
        self.__grade = grade

    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            # If finding out error stop the Python (can use try - except to catch error)
            raise ValueError('Number must be in 0 - 100')
        
    def get_grade(self):
        return self.__grade
    
    def display_info(self):
        print(f'Name: {self.name}, Score: {self.__grade}')

s1 = Student("Thuận", 85)
s2 = Student("Khang")
s3 = Student("Kiệt")

s1.display_info()
s2.display_info()

s2.set_grade(95)
s3.set_grade(70)

s2.display_info()
s3.display_info()

try:
    s3.set_grade(150)
except ValueError as e:
    print('Error:', e)