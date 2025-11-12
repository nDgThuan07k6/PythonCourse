# break: Used to terminate the loop entirely
# continue: Skips to the next iteration of the loop
# pass: Does nothing, acts as a placeholder\
while True:
    name = input('Please enter your name: ')
    if name != '':
        break               # If user enter name different from null it print their name and break

phone_number = '123-456-7890'
for i in phone_number:
    if i == '-':
        continue            # Skin '-'
    print(i, end='')        # Result: 1234567890
print()

for i in range (1, 5):
    if i == 3:
        pass
    else:
        print(i, end=' ')   # Result: 1245
