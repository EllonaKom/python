
n = int(input('Введите количество дней в рассматриваемом периоде: '))
t = []
for i in range(n):
    t.append(random.randint(-50, 50))
print(t)

# t = [38, 39, 21, 46, 38]

count1 = 0
result = 0
for i in range(len(t)):
    if t[i] > 0:
        count1 += 1
        if result < count1: result = count1
    if t[i] <= 0:
        count1 = 0
    # print(t[i], count1, result)
print(result)