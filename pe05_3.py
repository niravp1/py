numbers = [x*4 for x in range(0,11)]
numbers_2 = []

print(numbers)
for  x in numbers:

    new_num= x//2
    numbers_2.append(new_num)

print(numbers_2)

numbers_3 = numbers_2[::]

numbers_4= [] 
for x in numbers_2:
    b =x//2
    numbers_4.append(b)
print(numbers_4)


