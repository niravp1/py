# a) Create three stuInfo dictionaries
stuInfo1 = {'student 1': {'name': 'john', 'gpa': 4.9}}
stuInfo2 = {'student 2': {'name': 'myers', 'gpa': 3.1}}
stuInfo3 = {'student 3': {'name': 'tim', 'gpa': 2.0}}

# b) Create a list stuClass and add dictionaries
stuClass = [stuInfo1, stuInfo2, stuInfo3]

# c) Print the list of students
print("List of students:")
for i in range(len(stuClass)):
    print(f"Student {i+1}: {stuClass[i][f'student {i+1}']}")

# d) Use a loop to print all the gpa
print("\nAll GPAs:")
for i in range(len(stuClass)):
    print(f"Student {i+1} GPA: {stuClass[i][f'student {i+1}']['gpa']}")

# e) Change the last student's GPA to 4.0
stuClass[-1]['student 3']['gpa'] = 4.0

# f) Add a new student info to the list
stuClass.append({'student 4': {'name': 'David', 'gpa': 3.9}})

# g) Print all names and GPAs with proper format
print("\nNames and GPAs:")
for i in range(len(stuClass)):
    print(f"Student {i+1}: Name: {stuClass[i][f'student {i+1}']['name']}, GPA: {stuClass[i][f'student {i+1}']['gpa']}")

# Output everything in dictionary format
output_dict = {'students': stuClass}
print("\nOutput in dictionary format:")
print(output_dict)
