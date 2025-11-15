name = 'Nguyen Duong Gia Thuan'
string = 'tutorial'
temp = 'Tutorial'
number = '123'

# Print length of the string
print('Length of the string:', len(name))   # --> Length of the string: 22

# Find the position of character user entered
# Print -1 if no value found
print('Position of the character (B):', name.find('B'))     # Position of the character (B): -1
print('Position of the character (a):', name.find('a'))     # Position of the character (a): 15
# Using capitalize() to make string[0] capital and the other letter is lowercase

print('String after capitalize:', string.capitalize())      # String after capitalize: Tutorial

# Using upper() to uppercase all word
print('String after uppercase:', string.upper())            # String after uppercase: TUTORIAL

# Using lower() to lowercase all word
print('String after lowercase:', temp.lower())              # String after lowercase: tutorial

# Using isdigit() in order to check is it digit or not
print('Checking number:', number.isdigit())                 # Checking number: True

# Checking if character in string is from a-zA-Z include unicode by using isalpha()
print('Checking alpha:', string.isalpha())                  # Checking alpha: True

# Using count() to count character assigning in string
print('Number of character (t):', string.count('t'))        # Number of character (t): 2

# Using replace('firstCharacter','secondCharacter') in order to replace character
print('String before replace:', string)
print('String after replace:', string.replace('ial', 'y'))