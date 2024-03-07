#created list and printed the contents
courses = ["ET574", "PH111", "PH112", "Chemistry 101" ]
print(courses)
#using len function i then converted to str to print
print("I am taking "+ str(len(courses)) + " courses")
#prints the first course since it starts for 0
print(courses[0])
#prints last course which is "3"
print(courses[3])
#prints the list
print(courses[::])
#prints list but reverse 
print(courses[::-1])
#sliced from 1 to 3 which aligns with list values
print(courses[1:3])