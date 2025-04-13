# (МОДУЛЬ 4) год рождения А.С.Пушкина

year_of_birth = 1799

while True:

    year = int(input("Введите год рождения Александра Сергеевича Пушкина: "))

    if year == year_of_birth:
        print("Верно")
        break

    else:
        print("Неверно")


# Вариант с обработкой случая ввода не числового символа

year_of_birth = 1799

while True:
    try:
        year = int(input("Введите год рождения Александра Сергеевича Пушкина: "))

        if year == year_of_birth:
            print("Верно")
            break

        else:
            print("Неверно")

    except ValueError:
        print("Ошибка: Введите число, а не текст!")