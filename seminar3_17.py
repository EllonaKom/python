# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

nums = [1, 1, 2, 0, -1, 3, 4, 4]
result = []
for i in nums:
    if i not in result:
        result.append(i)
print(result)
print(len(result))