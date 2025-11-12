# copyfile(): copies contents if a file
# copy(): copyfile() + permission mode + destination can be a directory
# copy2(): copy() + copies metadata (file's creation and notification times)
# Using import shutil in order to use function
import shutil

# Using shutil.copyfile(file, copyfile) to create a copyfile from file
shutil.copyfile('c:\\Studybase\\Python\\Course\\data\\test.txt', 'c:\\Studybase\\Python\\Course\\data\\copy.txt')       # Make a copy.txt from test.txt

# copy() and copy2() same as like this