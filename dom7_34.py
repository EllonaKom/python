# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод:                                  Вывод:
# пара-ра-рам рам-пам-папам па-ра-па-дам Парам пам-пам



# s='пара-ра-рам рам-пам-папам па-ра-па-дам'

# print ('Парам пам-пам' if len(set([i.count('а') for i in s.split()]))==1 else 'Пам парам')

#s = input("Введите стихотворение: ")
s='пара-ра-рам рам-пам-папам па-ра-па-дам'
str = s.lower().split() 
if len(str) > 1:
    f = lambda x: sum(1 for i in x if i in "аеёиоуыэюя") 
    t = f(str[0]) 
    if all([f(i) == t for i in str]): 
        print("Парам пам-пам") 
    else: print("Пам парам")
else:
    print("Количество фраз должно быть больше одной!")

#     stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# list_1 = stroka.split(" ")
# glasn = ['а', 'е', 'и', 'о', 'у', 'э', 'ю', 'я', 'ё']
# res = list()
# def puh():
#     if len(list_1) == 1: return "Количество фраз должно быть больше одной!" 
#     else:
#         for i in list_1:
#             res.append(len([j for j in i if j in glasn]))
#         if len(set(res)) == 1:
#             return "Парам пам-пам"
#         else:
#             return "Пам парам"            
# print(puh())