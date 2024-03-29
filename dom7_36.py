# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.
# Ввод:                                     Вывод:
# print_operation_table(lambda x, y: x * y) 1 2 3 4 5 6
#  2 4 6 8 10 12
#  3 6 9 12 15 18
#  4 8 12 16 20 24
#  5 10 15 20 25 30
#  6 12 18 24 30 3
def print_operation_table(operation, num_rows=9, num_columns=9):
     for i in range(1, num_rows + 1):
         answer = []
         for j in range(1, num_columns + 1):
             answer.append(str(operation(i, j)))
         print(''.join(f'{e:<4}' for e in answer))

# def print_operation_table(operation, num_rows=6, num_columns=6):
#     a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
#     for i in a:
# print([''.join(f'{e:<4}' for x in i])
print_operation_table(lambda x, y: x * y)

# определение print_operation_table(операция, num_rows = 6, num_columns = 6): 
# для i в диапазоне(1, num_rows + 1): a = [] для j в диапазоне(1, num_columns + 1): a.append(str(операция(i, j))) print(" ".join(f"{e:<4}" для e в a)) 
# print_operation_table(лямбда x, y: x * y)

