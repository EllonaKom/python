# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

numN = int(input('Введите количество элементов в массиве '))
list_1 = [i for i in range(1,numN)]
print(list_1)

numX = int(input('Введите число X '))
kol = 0
rez = numN 
rezZ = 0

for j in list_1:
 
    kol = abs(j-numX)    
    if kol < rez: 
        rez = kol
        rezZ = j
        
#print(rez)
print(rezZ)
