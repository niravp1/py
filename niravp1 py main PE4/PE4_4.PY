grades= []
grades.extend([56, 82, 96, 58, 100])
print(grades)
total_grades = 0
for d in grades:
    total_grades += d
avg = total_grades/len(grades)
print(round(avg,2))

grade_sort = sorted(grades) 
del grade_sort[0:2]
print(grade_sort)

for x in grades:
    if x < 60:
        grades.remove(x)
print(grades)

print(round(sum(grades)/len(grades),3))






