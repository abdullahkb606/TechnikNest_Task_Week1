def LengthConversion():
    while True:
        print('\n--- Length Conversions ---')
        print('1. Meters to Feet')
        print('2. Feet to Meters')
        print('3. Kilometers to Miles')
        print('4. Miles to Kilometers')
        print('5. Centimeters to Inches')
        print('6. Inches to Centimeters')
        print('0. Back to Main Menu')

        choice = int(input('Choose a conversion: '))

        if choice == 0:
            break
        elif choice == 1:
            val = float(input("Enter meters: "))
            print(f"{val} m = {val * 3.28084:.2f} ft")
        elif choice == 2:
            val = float(input("Enter feet: "))
            print(f"{val} ft = {val / 3.28084:.2f} m")
        elif choice == 3:
            val = float(input("Enter kilometers: "))
            print(f"{val} km = {val * 0.621371:.2f} miles")
        elif choice == 4:
            val = float(input("Enter miles: "))
            print(f"{val} miles = {val / 0.621371:.2f} km")
        elif choice == 5:
            val = float(input("Enter centimeters: "))
            print(f"{val} cm = {val / 2.54:.2f} inches")
        elif choice == 6:
            val = float(input("Enter inches: "))
            print(f"{val} inches = {val * 2.54:.2f} cm")
        else:
            print("Invalid choice. Try again.")

def WeightConversion():
    while True:
        print('\n--- Weight Conversions ---')
        print('1. Kilograms to Pounds')
        print('2. Pounds to Kilograms')
        print('3. Grams to Ounces')
        print('4. Ounces to Grams')
        print('0. Back to Main Menu')

        choice = int(input('Choose a conversion: '))

        if choice == 0:
            break
        elif choice == 1:
            val = float(input("Enter kilograms: "))
            print(f"{val} kg = {val * 2.20462:.2f} lbs")
        elif choice == 2:
            val = float(input("Enter pounds: "))
            print(f"{val} lbs = {val / 2.20462:.2f} kg")
        elif choice == 3:
            val = float(input("Enter grams: "))
            print(f"{val} g = {val / 28.3495:.2f} oz")
        elif choice == 4:
            val = float(input("Enter ounces: "))
            print(f"{val} oz = {val * 28.3495:.2f} g")
        else:
            print("Invalid choice. Try again.")

def TemperatureConversion():
    while True:
        print('\n--- Temperature Conversions ---')
        print('1. Celsius to Fahrenheit')
        print('2. Fahrenheit to Celsius')
        print('3. Celsius to Kelvin')
        print('4. Kelvin to Celsius')
        print('0. Back to Main Menu')

        choice = int(input('Choose a conversion: '))

        if choice == 0:
            break
        elif choice == 1:
            val = float(input("Enter Celsius: "))
            print(f"{val}°C = {(val * 9/5) + 32:.2f}°F")
        elif choice == 2:
            val = float(input("Enter Fahrenheit: "))
            print(f"{val}°F = {(val - 32) * 5/9:.2f}°C")
        elif choice == 3:
            val = float(input("Enter Celsius: "))
            print(f"{val}°C = {val + 273.15:.2f} K")
        elif choice == 4:
            val = float(input("Enter Kelvin: "))
            print(f"{val} K = {val - 273.15:.2f}°C")
        else:
            print("Invalid choice. Try again.")

# --- Main Program ---
while True:
    print('\n====== UNIT CONVERTER ======')
    print('1. Length conversions')
    print('2. Weight conversions')
    print('3. Temperature conversions')
    print('0. Exit')
    
    try:
        choice = int(input('Enter your choice: '))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 0:
        print("Thanks for using the converter. Goodbye!")
        break
    elif choice == 1:
        LengthConversion()
    elif choice == 2:
        WeightConversion()
    elif choice == 3:
        TemperatureConversion()
    else:
        print("Invalid input. Please select from the menu.")

