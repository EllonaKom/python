# Найти факториал числа через рекурсию

def factor(num):
    if num == 0:  return 1
    return num * factor(num - 1)    
print(factor(6))