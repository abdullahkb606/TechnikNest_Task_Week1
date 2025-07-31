import random

full_name = input("Enter your full name: ")

name_parts = full_name.split()
rand_no = random.randint(10,99)

# Check if at least two parts exist
if len(name_parts) >= 2:
    first = name_parts[0].lower()
    last = name_parts[-1].lower()
    
    # Build a simple usernamE
    username = first + last
    print(f"Your username could be: {username}{rand_no}")
else:
    print("Please enter at least your first and last name.")

