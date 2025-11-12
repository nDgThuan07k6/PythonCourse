temp = 26
temperature = 29

# Using logical operators such as(and, or, not) to check two or more conditional statement
if temp >= 0 and temp <= 30:
    print('I gonna go outside!')        # 0 <= 26 <= 30 --> Print I gonna go outside!
elif temp < 0 or temp > 30:
    print('I gotta stay inside!')

if not(temperature >= 0 and temperature <= 30):
    print('I gonna go outside!')        # 29 < 30: False because not() --> No execute
elif not(temperature < 0 or temperature > 30):
    print('I gotta stay inside!')       # 29 < 30: True because nit() check the opposite --> Print I gotta stay inside! 