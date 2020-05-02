import re

text = input('Введите слова через пробел: ')
words = re.findall(r'\w+', text)

counter = 1
while words:
    word_list = []
    for i in words:
        if len(i) == counter:
            word_list.append(words.pop(words.index(i)))
    if word_list:
        print(f'Слова с количеством символов: {counter}')
        print(word_list)
    counter += 1