marks = int(input('Input Marks to know the grade: '))

print('Your Grade is: ')

if(marks >= 90 and marks<=100):
    print('A')
elif(marks<90 and marks>=80):
    print('B')
elif(marks<80 and marks>=70):
    print('C')
elif(marks<70 and marks>=60):
    print('D')
elif(marks<60 and marks >=0 ):
    print('F')
else:
    print('Invalid marks')
