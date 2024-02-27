first_num = int(input("Please enter the first integer:"))
second_num = int(input("Please enter the second integer:"))
third_num= int(input("Please enter the third integer:"))
totalnum = first_num, second_num, third_num
smallest = min(first_num, second_num, third_num)
largest = max(first_num, second_num, third_num)
middle = first_num + second_num + third_num - smallest - largest



print("Before Sorting:" + " " + str(totalnum))
print("After Sorting:" + " " + str(smallest) + str(middle) + str(largest))

