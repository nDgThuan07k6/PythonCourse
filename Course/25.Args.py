# *agrs is a a parameter that will pack all the arguments into the tuple
# A function can accept a varying amount of arguments
def add(number_one, number_two):
    sum = number_one + number_two
    return sum
print(add(1, 2))                        # Result: 3

# What if user wanna add more number in function
# print(add(1, 2, 3))                     # Result: TypeError: add() takes 2 positional arguments but 3 were given

# That why we switch to use *args
def addValue(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(addValue(1, 2, 3, 4))             # Result: 10

# If user wanna change something in *args they must cover tuple into list
def addNumber(*stuff):
    sum = 0
    stuff = list(stuff)
    stuff[0] = 10
    for i in stuff:
        sum += i
    return sum
print(addNumber(1, 2, 3, 4))            # Result: 19                