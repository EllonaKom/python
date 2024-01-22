# Напишите функцию, которая проверяет, является ли число простым.
# Число простое, которое имеем два делителя 1 и оно само.


def func(n,d = 2):
    if  d*d > n:           # n == 2 or n == d:      или
        return True
    elif n % d  == 0:
        return False
    return func(n, d + 1)    


print(func(21))
