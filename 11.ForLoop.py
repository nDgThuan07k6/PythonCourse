import time
age = 30

# Using for loop in order to execute a block of code in a limit amount of times (Limited)
# Structure 1: for <index> in range(<index>)
for i in range(10):
    print(i, end=' ')       # --> 0 1 2 3 4 5 6 7 8 9
print()

# Structure 2: for <index> in range(start, stop - 1)
for i in range(50, 60):
    print(i, end=' ')       # --> 50 51 52 53 54 55 56 57 58 59
print()

# Structure 3: for <index> in range(start, stop - 1, steps)
for i in range(50, 60, 2):
    print(i, end=' ')       # --> 50 52 54 56 58
print()

# Structure 4: for <index> in 'string'
for i in 'Thuan':
    print(i, end='')        # --> Thuan
print()

# Structure 5: Using time.sleep(<index>) so the loop will execute base on times
for i in range(3, 0, -1):
    time.sleep(1)
print('Happy New Year')     # After 3 seconds it print --> Happy New Year