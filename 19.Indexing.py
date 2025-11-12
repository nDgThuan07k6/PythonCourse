# Index operator []: Give access to a sequence's element (str, lists, tuples)
name = 'thuan Nguyen'

# Using index operator[].function() in order to check something
if(name[0].islower()):
    name = name.capitalize()
print(name)                             # Result: Thuan nguyen

# Using index operator[start:stop] in order to substring
first_name = name[:5].upper()
print(first_name)                       # Result: THUAN
last_name = name[6:].upper()
print(last_name)                        # Result: NGUYEN