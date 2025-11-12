# Return statement: Functions send python values/objects back to the caller
def multiply(number_one, number_two):
    result = number_one * number_two
    return result

def multiply(number_one, number_two):
    return number_one * number_two

# When user return value user must set that value to an objects
result = multiply(2, 3)
print(result)                               # Result: 6