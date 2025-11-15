# Tuple: Collection which is ordered and unchangeable, used to group together related data
# String = ('str', index, 'str')
Student = ('Thuan', 21, 'Male')

# Using count to count many time that string appear
print(Student.count('Thuan'))           # Result: 1

# Using index to find the position of the value in string
print(Student.index('Male'))            # Result: 2

for i in Student:
    print(i, end=' ')                   # Result: Thuan 21 Male
print()

if 'Thuan' in Student:
    print('Thuan is here!')             # Result: Thuan is here!