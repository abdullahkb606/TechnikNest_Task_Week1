# Ask user to enter principal amount
principal = float(input("Enter the principal amount: "))

# Ask user to enter annual interest rate
rate = float(input("Enter the annual interest rate (in %): "))

# Ask user to enter time period in years
time = float(input("Enter the time in years: "))

# Calculate simple interest using the formula
simple_interest = (principal * rate * time) / 100

# Print the calculated simple interest
print("The simple interest is:", simple_interest)
