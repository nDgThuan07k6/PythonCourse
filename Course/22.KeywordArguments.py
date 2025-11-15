# Keyword arguments: Arguments preceded by an identifier when we pass them to a function.
# Python autodetect the name of the arguments that our function receives
def helloName(first, middle, last):
    print('Hello', first, middle, last)

helloName(last='Thuan', first='Nguyen', middle='Duong Gia')         # Result: Hello Nguyen Duong Gia Thuan