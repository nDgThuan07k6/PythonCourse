age = 19

# Using if-else statement in order to execute if condition is true
if age < 1:
    print('You have not been born yet!!')   # 19 > 1 --> No execute
elif age < 18:
    print('You are not old enough!!')       # 19 > 18 --> No execute
else:
    print('You are an adult')               # --> Print you are an adult because 19 is the other cases