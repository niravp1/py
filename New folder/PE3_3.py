#Use int so that I can do the bmi function 

height = int(input("Please enter the height (in cm):"))
weight = int(input("Please enter the weight (in kg):"))
bmi = weight/height**2 * 703
print("BMI="+ " "+ str(bmi))