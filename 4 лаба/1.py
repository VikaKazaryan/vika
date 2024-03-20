def z1():
    def delit(x, y):
        if x % y == 0:
            return True
        else:
            return False
    x = int(input("введите число: "))
    y = int(input("введите число: "))
    if delit(x, y):
        print(x, "делится на", y)
    else:
        print(x, "не делится на", y)
z1()

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

def z3():
    date = input("Введите дату в формате ДД.ММ.ГГГГ: ")
    day, month, year = map(int, date.split('.'))
    if day * month == int(str(year)[-2:]):
        return True
    else:
        return False
print(z3())

def z4():
    def happy(x):
        sum1 = 0
        for i in range(len(x) // 2):
            sum1 += int(x[i])
        sum2 = 0
        for j in range(len(x) // 2, len(x)):
            sum2 += int(x[j])
        if sum1 == sum2:
            return "билет счастливый"
        else:
            return "повезет в другой раз"
    x = input("введите номер билета: ")
    if len(x) % 2 == 0:
        print(happy(x))
    else:
        print("Перезапустите программу и введите номер билета еще раз. В номере билета должно быть четное количество цифр!")
z4()