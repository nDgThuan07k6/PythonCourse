# Nested functions calls is calling function inside other functions
# Innermost function calls are resolved first
number = input('Enter a number: ')
number = float(number)
number = abs(number)
number = round(number)
print(number)

# Now is nested functions calls
print(round(abs(float(input('Enter a number: ')))))