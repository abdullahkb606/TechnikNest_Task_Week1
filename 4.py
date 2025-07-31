min = int(input('Enter the Minutes: '))

hours = int(min/60)
min_2 = min%60

print(f'Your entered minutes {min} are equal to: {hours}:{min_2} Hours')
