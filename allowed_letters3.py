# проверяет, содержитит ли выражение все заданные символы

def uses_only(word, allow_letters):
    for i in allow_letters:
        if i not in word:
            return 'выражение содержит не все заданные символы'
    return 'выражение содержит все заданные символы'


word = input('введите выражение: \n')
allow_letters = input('задайте список символов: \n')

print(uses_only(word, allow_letters))