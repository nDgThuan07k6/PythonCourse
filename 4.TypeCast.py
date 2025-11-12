x = 1
y = 2.0
z = '3'

# If user wanna typecast the value need to make sure that those can be typecast
print(float(x))     # --> 1.0
print(float(z))     # --> 3.0

#There are still some situation that user cannot be typecast
string = 'hello'
print(float(string))    # --> ValueError: could not convert string to float: 'hello'
