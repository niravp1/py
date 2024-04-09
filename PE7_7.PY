#crate blank list
list = []


#inifinte loop that converts string value from user to int
while True:
 a = int(input("Please enter a number or 0 to stop: "))
 #if statement that breaks loop if a == 0 or adds the input to the list if not 0 
 if a == 0:
   break
 else:
    list.append(a)
print(list)
print(sum(list))
#takes average by taking sum and dividing it by length
print(sum(list)/len(list))