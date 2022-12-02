# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 60 -> 2, 2, 3, 5

num = int(input("Введите число: "))
res=num
list =[]
for i in range(2, num):
    for j in range(2,num):
        if res % i == 0:
            list.append(i)
            res = res/i
print(num,'->',list)
