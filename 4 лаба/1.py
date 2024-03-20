def z1():
    def delit(x):
        if x % 5 == 0:
            return "Введенное число делится на 5"
        else:
            return False
    x = int(input("введите число: "))
    print(delit(x))
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
    def mag(x):
        if x[-2] == '0':
            chislo = x[-1]
        else:
            chislo = x[-2:]
        if x[0] == '0' and x[3] != '0':
            itog = int(x[1]) * int(x[3:5])
            if str(itog) == chislo:
                return True
            else:
                return False
        elif x[0] == '0' and x[3] == '0':
            itog = int(x[1]) * int(x[4])
            if str(itog) == chislo:
                return True
            else:
                return False
        elif x[0] != '0' and x[3] == '0':
            itog = int(x[:2]) * int(x[4])
            if str(itog) == chislo:
                return True
            else:
                return False
        elif x[0] != '0' and x[3] != '0':
            itog = int(x[:2]) * int(x[3:5])
            if str(itog) == chislo:
                return True
            else:
                return False
    x = input("введите дату (в формате ДД.ММ.ГГГГ): ")
    if len(x) == 10 and x[2] == '.' and x[5] == '.':
        print(mag(x))
    else:
        print("Ошибка! Перезапустите программу и введите дату правильно!")
z3()

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

