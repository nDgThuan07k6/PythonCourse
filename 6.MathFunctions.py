import math

x = 3.14
y = 3.54
z = 1
minus = -2

# Using round() in order to round number on or up base on decimal
print(round(x))         # --> 3
print(round(y))         # --> 4       

# Using math.ceil() in order to round number up
print(math.ceil(x))     # --> 4

# Using math.floor() in order to round number down
print(math.floor(y))    # --> 3

# Using abs() in order to get absolute value of a number
print(abs(minus))       # --> 2

# Using pow(number, time) in order to power n times
print(pow(minus, 2))    # --> 4

# Using math.sqrt() in order to get square root of that number
print(math.sqrt(400))   # --> 20.0
'''Or can assign variable in this case'''
print(int(math.sqrt(400)))  # --> 20

# Using max(), min() to fix min max
print(max(x, y, z))     # --> 3.54
print(min(x, y, z))     # --> 1