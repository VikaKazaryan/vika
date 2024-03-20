import random
n = 0
m = 0
while n < 3:
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    c = int(input(f"{a} + {b} = "))
    if a + b == c:
        print("Правильно!")
        m+=1
    else:
        print("Ответ неверный")
        n+=1
    print("Игра окончена. Правильных ответов: ", m)