#Takes user input convets it into int then puts these values into totalsum vairable. from tehre using min function finds the lowest value and max function for the largest value 
#then to find middle add all first_num second_num _third_num - smallest - largest which gives you the middle value. Then prints at the very bottom

first_num = int(input("Please enter the first integer:"))
second_num = int(input("Please enter the second integer:"))
third_num= int(input("Please enter the third integer:"))
totalnum = first_num, second_num, third_num
smallest = min(first_num, second_num, third_num)
largest = max(first_num, second_num, third_num)
middle = first_num + second_num + third_num - smallest - largest



print("Before Sorting:" + " " + str(totalnum))
print("After Sorting:" + " " + str(smallest) + str(middle) + str(largest))

