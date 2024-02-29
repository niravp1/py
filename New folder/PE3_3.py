#Use int so that I can do the bmi function and used **2 for exponent

height = int(input("Please enter the height (in cm):"))
weight = int(input("Please enter the weight (in kg):"))
bmi = weight/height**2 * 703
print("BMI="+ " "+ str(bmi))