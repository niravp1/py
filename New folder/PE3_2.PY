#used float to make decimal then used int to convert string and printed by converted int to str
bill = float(input("Enter the amount of the bill:"))
tip = int(input("Enter the percentage of tip:"))
value = bill * tip/100
print("Tip:"+" "+str(round(value,2)))