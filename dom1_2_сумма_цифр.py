# Задача 2: Найдите сумму цифр трехзначного числа. 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

num1= int(input('Введите трехзначное число '))

kol1 = num1//100 + num1 % 100 // 10 + num1 % 10
print( f'Сумма цифр  {kol1} ' )