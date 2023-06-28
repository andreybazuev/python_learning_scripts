# проверяет наличие запрещенных символов в выражении
def avoids(word, forb_letters):
    for i in forb_letters:
        if i in word:
            return 'выражение содержит запрещенные символы!'
    return 'выражение не содержит запрещенных символов'          

word = input('введите выражение: \n')
forb_letters = input('введите список запрещенных символов: \n')

print(avoids(word, forb_letters))
