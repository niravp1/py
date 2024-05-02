# Create three stuInfo dictionaries
stu1 = {'name': 'John', 'gpa': 4.9}
stu2 = {'name': 'Myers', 'gpa': 3.1}
stu3 = {'name': 'Tim', 'gpa': 2.0}

# Create a list stuClass and add dictionaries
stuClass = [stu1, stu2, stu3]

# Print the list of students
print("List of students:")
for student in stuClass:
    print(student)

# Use a loop to print all the GPAs
print("\nAll GPAs:")
for student in stuClass:
    print(student['gpa'],end="|")

# Change the last student's GPA to 4.0
stuClass[-1]['gpa'] = 4.0
print("\nNames and GPAs:")

for student in stuClass:
    print(f"Name: {student['name']}, GPA: {student['gpa']}")

# Add a new student info to the list
stuClass.append({'name': 'David', 'gpa': 3.9})

#  all names and GPAs with proper format

# Updated Information
print("\nUpdated Information:")
for student in stuClass:
    print(f"- {student['name']}\t\t {student['gpa']}")

