# Ввести два числа
num1= int(input('Введите первое число:  '))
num2= int(input('Введите второе число:  '))

if num1 > num2:
    print(num1, f'num1= {num1} > num2= {num2}')
elif num1<num2:
    print(num2, f'num1= {num1} < num2= {num2}')
elif num1 == num2:
    print( f'num1= {num1} = num2= {num2}' )

