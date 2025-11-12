# Function is a block of code only executed when it is called
# Calling function by using def string(string, numeric, ...):
def hello():
    print('Hello World!')

hello()                         # Result: Hello World!

# Add string to function in order to call that string in function
def helloName(name):
    print('Hello', name)

helloName('Thuan')              # Result: Hello Thuan