# Dictionary: A changeable, unordered collection of the unique key:value pairs
# Using hashing in order to access data quickly
capitals = {'USA':'WashingtonDC', 
            'India':'NewDehli', 
            'China':'Beijing', 
            'Russia':'Moscow'}
print(capitals['China'])                # Print the value of the key --> Result: Beijing

# If the key is not available print error
print(capitals['Germany'])              # No value of the key --> Result: KeyError: 'Germany'

# Using .get(key) in order to check if the key is available in dictionaries or not
print(capitals.get('Germany'))          # No value of the key -->  Result: None

# Using .items() to print all the dictionary
print(capitals.items())                 # Result: dict_items([('USA', 'WashingtonDC'), ('India', 'NewDehli'), ('China', 'Beijing'), ('Russia', 'Moscow')]

# Also can use loop to print all the items
for key, value in capitals.items():
    print(key, value, end=' ')          # Result: USA WashingtonDC India NewDehli China Beijing Russia Moscow
print()

# Using .update({key:value}) in order to add value in dictionaries
capitals.update({'Germany':'Berlin'})
print(capitals.items())                 # Result: dict_items([('USA', 'WashingtonDC'), ('India', 'NewDehli'), ('China', 'Beijing'), ('Russia', 'Moscow'), ('Germany', 'Berlin')])

# Using .pop(key) in order to remove key:value of that element in the dictionaries
capitals.pop('Germany')
print(capitals.items())                 # Result: dict_items([('USA', 'WashingtonDC'), ('India', 'NewDehli'), ('China', 'Beijing'), ('Russia', 'Moscow')])

# Using .clear() in order to clear all the dictionaries
capitals.clear()