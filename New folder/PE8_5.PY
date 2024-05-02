rank = {1: "Freshman", 2: "Sophomore", 3: "Junior", 4: "Senior"}

years_input = input("Enter number of years: ")

#  if input is a valid integer
if years_input.isdigit():
    years = int(years_input)
    #  if input is within valid range
    if 1 <= years <= 4:
        # corresponding value from the dictionary
        print("You are a " + rank[years])
    else:
        print("Error: Invalid input. Please enter a number between 1 and 4.")
else:
    print("Error: Invalid input. Please enter a valid integer.")
