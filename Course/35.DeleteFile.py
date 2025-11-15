import os
import shutil
path = 'c:\\Studybase\\Python\\Course\\data\\test.txt'

# Using os.remove(file_name) in order to delete a file
os.remove(path)                         # Result: There is no test.txt file available

# Using os.rmdir(path) in order to delete a file or empty folder of that folder
# Using shutil.rmtree(path) in order to delete or files and folders in that folder