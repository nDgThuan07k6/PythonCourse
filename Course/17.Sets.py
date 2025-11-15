# Set: Collection which is unordered, unindex. Using for remove duplication values
utensils = {'fork', 'spoon', 'knife', 'knife', 'knife'}

for x in utensils:
    print(x, end=' ')                   # Randomly result: spoon fork knife
print()

# Used .add('str') in order to add something to set
utensils.add('napkin')
for x in utensils:
    print(x, end=' ')                   # Randomly result: spoon fork knife napkin
print()

# Used .remove('str') in order to remove something from set
utensils.remove('knife')
for x in utensils:
    print(x, end=' ')                   # Randomly result: spoon fork napkin
print()

# Used .clear() in order to remove all of the element from set
utensils.clear()

# Used .update('value') in order to add that value to another value
dishes = {'bowl', 'plate', 'cup'}
utensils.update(dishes)
for x in utensils:
    print(x, end=' ')                   # Randomly result: plate bowl cup
print()

# Used .difference('value') in order to find the difference between two value
utensils.add('knife')
print(utensils.difference(dishes))      # Result: {'knife'}

# Used .intersection('value') in order to find the same as thing in two value
print(utensils.intersection(dishes))    # Result: {'cup', 'bowl', 'plate'}