student = {
  "name": "An",
  "age": 21,
  "major": "Computer Science"
}

print(f'Student name: {student["name"]}')
student["age"] = 22
student['GPA'] = 3.5

#use del for delete value
del student['major']
print(student)