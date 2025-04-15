# (МОДУЛЬ 3) год и день рождения А.С.Пушкина

year_of_birth = 1799
birthday = 29

year = int(input("Введите год рождения Александра Сергеевича Пушкина: "))

if year != year_of_birth:
    print("Неверный год")

else:
    print("Верно")
    birth_day = int(input("Введите день рождения Александра Сергеевича Пушкина (по Юлианскому календарю): "))

    if birth_day != birthday:
        print("Неверный день рождения")
    else:
        print("Верно")