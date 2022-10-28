# Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.
# 7 –> 0 1 1 2 3 5 8

n = int(input("Введите число: "))
a = 0
b = 1
data = open('Fibonacci.txt', 'w')
data.writelines(str(n) + ' -> ' +  str(a) + (' ') + str(b))
for i in range(3, n+1):
    i = a+b
    data.writelines((' ') + str(i))
    a = b
    b = i
data.close()



