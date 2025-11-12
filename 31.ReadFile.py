# If user wanna read a file use with open(path) as name
with open('c:\\Studybase\\Python\\Course\\data\\test.txt') as file:
    # Using name.read() in order to read the file
    print(file.read())                          # Result: Hello my name is Thuan

# Using exception FileNotFoundError in order to check if the file is available