# В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.

let = (input('Введите букву: '))
data = open('frukt.txt', encoding = 'utf-8')
text = data.readlines()
data.close
for i in text:
    if i[0].lower() == let.lower():
        print(i,end='')


