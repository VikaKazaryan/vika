str = ""
while True:
    slovo = input("Введите слово: ")
    if slovo == "stop":
        break
    str = str + " " + slovo
print(str)