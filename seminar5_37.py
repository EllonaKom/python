# Задача №37.
# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
# Input: 2 -> 3 4  Output: 4 3

x = 4

def reverse(n):
    if n == 0: return "+"
    a = input("Введите число ")
    return  reverse(n - 1) + a

print(reverse(x))