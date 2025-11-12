# Exception are events detected during execution that interrupt the flow of a program
# Using try: except Exception: in order to detect
try:
    numerator = int(input('Enter a number to divide: '))
    denominator = int(input('Enter a number to divide by: '))
    result = numerator / denominator

# ZeroDivisionError in order to check if it divided by zero or not
except ZeroDivisionError:
    print('You cannot divide by zero!!')

# ValueError in order to check if the input is the string or not
except ValueError:
    print('You cannot divided by string!!')
except:
    print('Something went wrong')
else:
    print(result)

# Using finally: in order to check if it execute to the final part or not
finally:
    print('Executed successfully')

# If user want to set the exception as something to check the invalid literal use: as <index>
try:
    numerator = int(input('Enter a number to divide: '))
    denominator = int(input('Enter a number to divide by: '))
    result = numerator / denominator
    print(result)

except ZeroDivisionError as e:
    print(e)