# Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input("Введите число: "))
print(number, '->', end=" ")
count = 1
list = []
for i in range(1, number+1):
    count *= i
    list.append(count)
print(list)
