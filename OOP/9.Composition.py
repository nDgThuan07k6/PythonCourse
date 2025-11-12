class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def totalSalary(self):
        return self.pay + self.bonus

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Employee class using class totalSalary as an object
    def totalCompensation(self):
        return self.salary.totalSalary()
    
    def __str__(self):
        return f'{self.name} earns a total of ${self.totalCompensation()} per year.'
    
salary = Salary(50000, 10000)
emp1 = Employee('Kiet', salary)
print(emp1)