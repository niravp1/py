numbers = [x*4 for x in range(0,11)]
numbers_2 = []
numbers_3 = []

print(numbers)
for  x in numbers:
    new_num= x//2
    numbers_2.append(new_num)
print(numbers_2)


for x in numbers_2[:]:
   new_num2= x//2
numbers_3.append(new_num2)
print(numbers_3)
