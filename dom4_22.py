# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

# #.intersection() &
# list1 = list()
# list2 = list()


# numN = int(input('Введите количество элементов в 1 массиве '))

# numM = int(input('Введите количество элементов во 2 массиве '))
# print('Введите элементы 1 массива ')
# for i in range(numN):
#     list1.append(int(input()))
# print('Введите элементы 2 массива ')
# for i in range(numM):    
#     list2.append(int(input()))
# print(list1)
# print(list2)
# list1 = set(list1)
# list2 = set(list2)
# ll = sorted(list1.intersection(list2))
# print(ll)

 # для автотестов
var1 = '5 4' 
var2 = '1 3 5 7 9' 
var3 = '2 3 4 5' 
var1 = var1.replace(',', ' ').split()
print(var1)
var2= var2.replace('.', ' ').split()
print(var2)
var3= var3.replace('.', ' ').split()
print(var3)

var1 = [int(item) for item in var1]
print(var1)
var2 = [int(item) for item in var2]
print(var2)
var3 = [int(item) for item in var3]
print(var2)

list2 = set(var2)
list3 = set(var3)
ll = sorted(list2.intersection(list3))
print(*ll)