# Задача 1. Дано натуральное число N. Найдите значение выражения N + NN + NNN
# N может быть любой длины.
# N = 132 132 + 132132 + 132132132 = 132264396

n = input("Введите число: ")
print(n,'+',n*2,'+',n*3,'=', int(n)+int(n*2)+int(n*3))