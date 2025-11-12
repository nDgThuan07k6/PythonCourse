firstNumber = int(input('Input FirstNumber: '))
if firstNumber > 0:
    print('Positive number')
elif firstNumber < 0:
    print('Negative number')
else:
    print('Zero')
print('-------------------------------------------------------')
secondNumber = int(input('Input secondNumber: '))
match secondNumber:
    case x if x > 0:
        print('Positive number')
    case x if x < 0:
        print('Negative number')
    case x if x == 0:
        print('Zero')


