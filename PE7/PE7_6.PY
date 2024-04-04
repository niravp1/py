import random
integer = int( input("Enter an integer from 1-100: "))
grades = []
for x in range (integer):
    grades.append(random.randint(0,100))

pass_int = int( input("Enter a passing grade from 1-100 "))
pass_grades = []

for x in grades:
    if x> pass_int:
        pass_grades.append(x)

print(grades)
print(pass_grades)


