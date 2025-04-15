# (МОДУЛЬ 6) Викторина: год рождения поэта (можно использовать любые средства! так написано в задании)

dict_poet = {"А.С. Пушкин": 1799,
             "М.Ю. Лермонтов": 1814,
             "С.А. Есенин": 1895,
             "А.А. Блок": 1880,
             "Б.Л. Пастернак": 1890}   # словарь с фамилиями и годом рождения

right_answer = 0 # счётчик правильных ответов
incorrect_answer = 0 # счётчие неверных ответов

while True:

    for key, value in dict_poet.items(): # цикл по ключу и значению словаря

        year = int(input("Введите год рождения " + key + "а:  "))

        if year != value:
            print("Неверно")
            incorrect_answer += 1 # считаем неверные ответы

        else:
            print("Верно")
            right_answer += 1 # считаем верные ответы
            continue

    print("\n*****************************\n")
    print("Количество правильных ответов - ", right_answer)
    print("Количество ошибок - ", incorrect_answer)
    print("Процент правильных ответов - ", right_answer*100/5, " %")
    print("Процент неправильных ответов - ", 100 - right_answer*100/5, " %")

    beginning = input("Хотите начать игру с налала (да/нет)?: ")

    if beginning == "да":
        print("\n...Новая игра...")

    else:
        break