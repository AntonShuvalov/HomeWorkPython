# Создайте скрипт бота, который находит ответы на фразы по ключу в словаре.
# Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут».
# Если фраза ему неизвестна, он выводит соответствующую фразу.
# «как тебя зовут?» –> меня зовут Анатолий

dictionary = {'привет': 'Здравствуй, человек',
              'как тебя зовут?': 'Меня зовут Анатолий', 
              'кто ты?': 'Я Бэтмен'}
out = 1
while out == 1:
    ask = input('Пользователь: ')
    if ask.lower() in dictionary.keys():
        print('Бот:', dictionary[ask.lower()])
    elif ask.lower() == 'стоп':
        out = 0
    else:
        print("Бот: Ответа не знаю и обучаться не буду")
