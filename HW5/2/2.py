# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа, описывающие возрастающую последовательность.
#  Порядок элементов менять нельзя. [1, 5, 2, 3, 4, 6, 1, 7] =>[1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

import random
n = int(input("Введите количество чисел: "))
array = [random.randint(1, 50) for i in range(n)]
print(array)
index = random.randint(0, n-1)
res = [array[index]]
while index < n:
    index += 1
    if index < n:
        if array[index] > res[-1]:
            res.append(array[index])
print(res)
