# Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

text_1 = input('Введите первую строку: ')
text_2 = input('Введите вторую строку: ')
count = 0
for i in range(len(text_1)):
    for j in range(len(text_2)):
        if text_2[j] == text_1[i]:
            count += 1
    print(text_1[i], '-', count, end=", ")
    count = 0
