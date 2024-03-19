
#prints the list of 1-4 not including 5
a = list(range(5))
print(a)
#b is an empty list for and for each value in 1-4 it adds to list then prints b
b = []
for i in range (5):
 b.append(i)
print(b)
#prints from -10 9 and finds the min max and sum by using different methods
x = list(range(-10, 10))
print(x)
print(min(x), max(x), sum(x))

#finds even number from beginning which is 2 and 10 when you look from the right of list
even_num = list(range(2, 11, 2))
print(even_num[0], even_num[-1])

#this starts at 1 and goes up by 2 for all the odd numbers
odd_num = list(range(1,10,2))
print(odd_num)

#for each value of x it prints it cubed
for x in range(1,11):
 print(x**3)
#list comprehension does the same thing but in one line used "*" to make each element of a list an argument to add |
numbers = [x**3 for x in range(1,11)]
print(*numbers, sep= "|")


