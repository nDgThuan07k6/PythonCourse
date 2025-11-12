class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f'Employee: {self.name}, Salary: {self.salary}'

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def __str__(self):
        return f'Manager: {self.name}, Salary: {self.salary}, Department: {self.department}'

class Executive(Manager):
    def __init__(self, name, salary, department, stock_options):
        super().__init__(name, salary, department)
        self.stock_options = stock_options

    def __str__(self):
        return (f'Executive: {self.name}, Salary: {self.salary}, '
                f'Department: {self.department}, Stock Options: {self.stock_options}')

emp = Employee("Thuan", 50000)
mgr = Manager("Kiet", 70000, "IT")
exe = Executive("Quang", 120000, "Finance", 500)

print(emp)
print(mgr)
print(exe)