from tkinter import *
from tkinter import ttk

names = ['Алексеев Сергей Викторович', 'Баранов Николай Олегович', 'Ветров Игорь Николаевич']
tel = ['+79120057895','+79225481255','+79015731279']

def addTel():
    global names
    global tel
    name = input("Введите ФИО: ")
    telephone = input("Введите номер телефона: ") + '\n'
    names.append(name)
    tel.append(telephone)
    return 'Контакт добавлен'

def printTel():
    global names
    global tel
    list =[]
    for i in range(len(names)):
        list.append(names[i])
        list.append(tel[i])
    print(list)

def saveHTML():
    global names
    global tel
    book = open('book.html', 'w', encoding='utf-8')
    for i in range(len(names)):
        book.write(names[i])
        book.write(' ')
        book.write(tel[i])
    return 'Файл html добавлен'

def saveXML():
    global names
    global tel
    book = open('book.xml', 'w', encoding='utf-8')
    for i in range(len(names)):
        book.write(names[i])
        book.write(' ')
        book.write(tel[i])
    return 'Файл xml добавлен'

def newMenu():
    global root
    global frm
    root = Tk()
    root.title('PhoneBook')
    frm = ttk.Frame(root, padding=15)
    frm.grid()
    # ttk.Label(frm, text='Телефонный справочник\n').grid(column=1, row=1)
    ttk.Button(frm, text="Показать контакты", command=printNum).grid(column=0, row=6)
    ttk.Button(frm, text="Импорт в html", command=newHTML).grid(column=2, row=6)
    ttk.Button(frm, text="Добавить контакт", command=newTel).grid(column=0, row=7)
    ttk.Button(frm, text="Импорт в xml", command=newXML).grid(column=2, row=7)
    # ttk.Button(frm, text="Выход", command=root.destroy).grid(column=1, row=8)
    root.mainloop()

def printNum():
    global frm
    ttk.Label(frm, text=f'{printTel()}').grid(column=0, row=2)

def newHTML():
    global frm
    a = ttk.Label(frm, text=f'{saveHTML()}').grid(column=0, row=3)  

def newXML():
    global frm
    a = ttk.Label(frm, text=f'{saveXML()}').grid(column=0, row=4)  

def newTel():
    global frm
    ttk.Label(frm, text=f'{addTel()}').grid(column=0, row=5)

newMenu()
printNum()
newHTML()
newXML()

