#.format() is optional method that gives users control when displaying output
animal = 'cow'
item = 'moon'
print('The', animal, 'jumped over the', item)                                   # Result: The cow jumped over the moon

# User can use {} instead of instantly write in the print
print('The {} jumped over the {}'.format(animal, item))                         # Result: The cow jumped over the moon

# User can also use keyword method to insert by using key:value {key}
print('The {animal} jumped over the {item}'.format(animal='cow', item='moon'))  # Result: The cow jumped over the moon

name = 'Thuan'
print('Hello my name is {}'.format(name))                               # Result: Hello my name is Thuan

# User can use {:index} in order to add more space after that word
print('Hello my name is {:10}'.format(name))                            # Result: Hello my name is Thuan     

# There are some index in order to align the word
print('Hello my name is {:<10}. Nice to meet you!'.format(name))        # Result: Hello my name is Thuan     . Nice to meet you!
print('Hello my name is {:>10}. Nice to meet you!'.format(name))        # Result: Hello my name is      Thuan. Nice to meet you!
print('Hello my name is {:^10}. Nice to meet you!'.format(name))        # This case in centering word --> Result: Hello my name is   Thuan   . Nice to meet you!
'''------------------------------NUMBER----------------------------------------------------------------------------------------------------'''
number = 3.14159
print('The number pi is {}'.format(number))                         # Result: The number pi is 3.14159

# Add {:.<index>f} to upper how many after comma
print('The number pi is {:.2f}'.format(number))                     # Result: The number pi is 3.14

num = 1000
# Use {:,} in order to auto split after three zero
print('The number pi is {:,}'.format(num))                          # Result: The number pi is 1,000

# Use {:b} {:o} {:x} in order to print binary
print('The number pi is {:b}'.format(num))                          # Result: The number pi is 1111101000
print('The number pi is {:o}'.format(num))                          # Result: The number pi is 1750
print('The number pi is {:x}'.format(num))                          # Result: The number pi is 3e8
print('The number pi is {:e}'.format(num))                          # Result: The number pi is 1.000000e+03