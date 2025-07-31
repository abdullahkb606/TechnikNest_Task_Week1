# Ask user to enter their weight
weight = float(input("Enter your weight in kg: "))

# Ask user to enter their height
height = float(input("Enter your height in meters: "))

# Calculate BMI using the formula
bmi = weight / (height ** 2)

# Print the calculated BMI
print("Your BMI is:", round(bmi, 2))
