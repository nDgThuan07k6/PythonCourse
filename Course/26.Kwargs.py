# Kwargs is parameter that will pack all arguments into a dictionary
# Very useful so that a function can accept a varying amount of key arguments
def helloName(first_name, last_name):
    print('Hello', first_name, last_name)
helloName(first_name='Nguyen', middle_name='Duong Gia', last_name='Thuan')  # Result: TypeError: helloName() got an unexpected keyword argument 'middle_name'

# In order to fix that we use **kwargs
def hello(**kwargs):
    print('Hello', end=' ')
    for key, value in kwargs.items():
        print(value, end=' ')
hello(first_name='Nguyen', middle_name='Duong Gia', last_name='Thuan')      # Result: Hello Nguyen Duong Gia Thuan 