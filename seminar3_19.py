# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

# my_dict = [1, 2, 3, 4, 5] 
# k = 3
# print(my_dict[k-1:] + my_dict[:k-1])

my_dict = [1, 2, 3, 4, 5] 
k = 3
while k > 0:
    temp = my_dict.pop()
    my_dict.insert(0,temp)
    k -= 1
     
print(my_dict)    