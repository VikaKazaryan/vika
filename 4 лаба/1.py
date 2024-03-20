def task1():
    def delit(x):
        if x % 5 == 0:
            return "Введенное число делится на 5"
        else:
            return False
    x = int(input("введите число: "))
    print(delit(x))
task1()