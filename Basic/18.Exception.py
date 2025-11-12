try:
    numerator = float(input('Input numerator: '))
    denominator = float(input('Input denominator: '))
    result = numerator / denominator
    print(f'Print result: {result}')

except ZeroDivisionError:
    print('Error: Cannot divise zero')

except ValueError:
    print('Error: Please enter available number')

except Exception as e:
    print('There is an error cannot define', e)