# проверяет, состоит ли выражение из заданных символов

def uses_only(word, allow_letters):
    for i in word:
        if i not in allow_letters:
            return 'выражение содержит не заданные символы'
    return 'выражение состоит из заданных символов'


word = input('введите выражение: \n')
allow_letters = input('задайте список символов: \n')

print(uses_only(word, allow_letters))