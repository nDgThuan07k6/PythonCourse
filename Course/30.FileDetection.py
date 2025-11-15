# User need to import os in order to check the directory of the file
import os

# Using \\ instead of \ in order to use directory in os
path = 'C:\\Studybase\\Python\\Course\\data\\test.txt'

# Using os.path.exists(path) in order to check if location exists or not
if os.path.exists(path):
    print('That location exists!')                       # Result: That location exists!
    # Using os.path.isfile(path) in order to check if the file exists or not
    if os.path.isfile(path):
        print('That file exists too!')                   # Result: That file exists too!
    # Using os.path.isdir(path) in order to check if that folder exists or not
    elif os.path.isdir(path):
        print('That folder exists!')                     # Result: Print nothing cause there is no folder name test.txt
else:
    print('That location does not exist!')