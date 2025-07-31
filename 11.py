# Multiplication Table
num = int(input('Enter the number for obataining Multiplication Table: '))

for i in range (0,11):
    print(f'{num} X {i} = {num*i}')

# Sum numbers divisible by 3

input = int(input('Enter the range for which you want to obtain the result: '))

sum = 0

for i in range(0, input):
    if i%3 == 0:
        sum+=i

print(f'The sum of all numbers divisible by 3 in your provided range is {sum}.')
