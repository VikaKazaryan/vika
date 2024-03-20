def z2():
    def delit(x):
        itog = 300 / x
        return itog
    try:
        x = int(input("введите число: "))
        print(delit(x))
    except ValueError:
        print("Ошибка! Введено не число!")
    except ZeroDivisionError:
        print("Ошибка! Деление на 0 невозможно!")
z2()