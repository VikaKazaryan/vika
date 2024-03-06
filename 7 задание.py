words = []
while True:
    word = input('Введите слово')
    if word == 'stop':
        break
    words.append(word)
results = ' ' .join(words)
print(results)