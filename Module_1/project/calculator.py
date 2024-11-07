print("Welcome to Basic Calculator")
print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')

option = int(input('Select a option for basic calculator operation: '))

if option==1:
    n1 = int(input('Enter 1st number: '))
    n2 = int(input('Enter 2nd number: '))
    n3 = n1+n2
    print('Addition is: '+str(n3))
elif option==2:
    n1 = int(input('Enter 1st number: '))
    n2 = int(input('Enter 2nd number: '))
    n3 = n1-n2
    print('Subtraction is: '+str(n3))
elif option==3:
    n1 = int(input('Enter 1st number: '))
    n2 = int(input('Enter 2nd number: '))
    n3 = n1*n2
    print('Multiplication is: '+str(n3))
elif option==4:
    n1 = int(input('Enter 1st number: '))
    n2 = int(input('Enter 2nd number: '))
    n3 = n1/n2
    print('Divison is: '+str(n3))
else:
    print('Invalid input')