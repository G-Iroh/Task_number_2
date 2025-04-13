# (МОДУЛЬ 3) год рождения А.С.Пушкина
from jinja2.nodes import Break

year_of_birth = 1799
birthday = 29

while True:

    year = int(input("Введите год рождения Александра Сергеевича Пушкина: "))

    if year != year_of_birth:
        print("Неверный год")

    else:
        print("Верно")

        while True:
            birth_day = int(input("Введите день рождения Александра Сергеевича Пушкина (по Юлианскому календарю): "))

            if birth_day != birthday:
                print("Неверный день рождения")

            else:
                print("Верно")
                break
        break