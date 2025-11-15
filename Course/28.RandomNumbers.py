# Using radom library in order to use random stuff
import random
# Use random.randint(range, range) in order to generate random integer
x = random.randint(1, 6)
print(x)                            # Result: Random from 1 to 6

# Use random.random() in order to generate random number from 0 to 1
y = random.random()
print(y)                            # Result: Some float from 0 to 1

myList = ['Rock', 'Paper', 'Scissor']
# Using random.choice(list) in order to generate random string in that list
z = random.choice(myList)
print(z)                            # Result: Randomly rock, paper, scissor

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
# Using random.shuffle(list) in order to shuffle the list
random.shuffle(cards)
print(cards)                        # Result: Some random result like: [6, 'J', 9, 5, 10, 'A', 4, 8, 'Q', 'K', 3, 2, 7]