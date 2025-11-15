name = 'Thuan'

# Getting a character by extracting elements from another string by using index[i]
print('First character:', name[0])          # --> First character: T

# Create a substring by extracting elements from another string by using index[start:stop:steps]
print('Two character:', name[0:2])          # --> Two character: Th
print('String:', name[3:5])                 # --? String: an

# If value start from zero user do not to enter 0 at start, leave blank
print('Two character:', name[:2])           # --> Two character: Th

# Add step if user wanna print step n of the string
print('String step 2:', name[::2])         # --> String step 2: Tun

# Reverse a string by set steps = -1
print('Reverse name:', name[::-1])          # --> Reverse name: nauhT

'''---------------ANOTHER WAY OF CREATE A SUBSTRING------------------'''
website = 'https:://google.com'
world_wide_web = 'https:://wikipedia.com'
# Using slice(start, stop, steps) to create a substring
# Attention: Positive number will get position start from the left and negative number will get the position start from the right
slice = slice(9, -4)    # 9 is positive number so it start getting from g opposite of -4
print('Output name of the website:', website[slice])                # --> Output name of the website: google
print('Output name of the website:', world_wide_web[slice])         # --> Output name of the website: wikipedia



