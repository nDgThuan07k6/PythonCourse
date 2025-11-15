# Assign value (value do not need to set type before assign, Python define it automatically)
name = 'Nguyen Duong Gia Thuan'
age = 19
height = 1.72
human = True
print('Name:', name)
print('Age:', age)
print('Height:', height)
print('Is it human:', human)
# In python if user wanna know what type of value they can use type()
print(type(name))           # --> Type: String
print(type(age))            # --> Type: Int
print(type(height))         # --> Type: Float
print(type(human))          # --> Type: Boolean

'''-------------------------------------------------------------------------------'''
object = 'Student'
# In Python print print string and plus another string do not include space
print('I am' + object)      # --> I amStudent
print('I am ' + object)     # --> I am Student

# In Python print string and put comma after that with a string it will automatically include space
print('I am', object)       # --> I am Student

# Of course if user wanna print some thing else except string that value must be covered into string
# This situation is the only issue when user using plus not comma
total = 32
print('Number of students:', total)         # --> Number of students: 32 (No error include)
print('Number of students: ' + str(total))  # --> Number of students: 32
print('Number of students: ' + total)       # --> TypeError: can only concatenate str (not "int") to str

