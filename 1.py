# Collect user profile data
name = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender (Male/Female/Other): ")
city = input("Enter your city: ")
hobby = input("Enter your favorite hobby: ")

# Print a typed profile summary
print("\n--- User Profile Summary ---")
print(f"Name: {name}")
print(f"Age: {age} years old")
print(f"Gender: {gender}")
print(f"City: {city}")
print(f"Hobby: {hobby}")
print(f"{name} is a {age}-year-old {gender.lower()} from {city}, who enjoys {hobby.lower()}.")
