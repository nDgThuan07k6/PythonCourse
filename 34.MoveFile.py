# Using import os in order to move a file
import os
source = 'c:\\Studybase\\Python\\Course\\data\\test.txt'
destination = 'c:\\Studybase\\Python\\Course\\data'
# Using os.replace(source, destination) in order to move a file
os.replace(source, destination)                     # Result: See a file in destination already