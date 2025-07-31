import string

password = input("Enter your password: ")

score = 0

# Conditions
if len(password) >= 8:
    score += 1  # Good length

if any(char.islower() for char in password):
    score += 1  # Has lowercase

if any(char.isupper() for char in password):
    score += 1  # Has uppercase

if any(char.isdigit() for char in password):
    score += 1  # Has numbers

if any(char in string.punctuation for char in password):
    score += 1  # Has special characters 

# Classify based on score
if score == 5:
    strength = "Very Strong"
elif score == 4:
    strength = "Strong"
elif score == 3:
    strength = "Moderate"
elif score == 2:
    strength = "Weak"
else:
    strength = "Very Weak"

print(f"Your password strength is: {strength}")
