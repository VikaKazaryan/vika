n = int(input("Количество слов: "))
stroka = ""
while n > 0:
    slovo = str(input("Введите слово: "))
    stroka = stroka + " " + slovo
    n-= 1
print(stroka)