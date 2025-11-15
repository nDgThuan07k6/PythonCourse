# Lists: used to store multiple items in a single variable
# Architect: ['sth', 'sth']
food = ["pizza", "hamburger", "spagetti"]
print(food[0])              # Result: pizza
print(food[5])              # Result: IndexError: list index out of range

food[0] = 'sushi'
print(food[0])              # Food[0] update --> Result: sushi

# If user wanna bring all the items in the lists use loop
for i in food:
    print(i, end=' ')       # Result: sushi hamburger spagetti
print()

# Add element to the end of the list
food.append('ice cream')
print(food[3])              # Result: ice cream

# Remove element in the list
food.remove('ice cream')
print(food[3])              # Result: IndexError: list index out of range
print()

# Remove the last element in the list
food.pop()

# Insert the element by using .insert(index, 'string')
food.insert(1, 'pie')
print(food[1])              # Result: pie
print()

# Using .sort in order to sort the list in alphabet
food.sort()

# Clear the list by using .clear()
food.clear()                # Result: The list is empty