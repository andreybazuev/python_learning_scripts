#Сравнение строк можно использовать для сортировки в алф. порядке
word = 'арбуз'
word2 = 'Банан'

word = word.lower() #все в строчные, т.к. заглавные всегда перед строчными
word2 = word2.lower()

if word < word2:
    print('Cлово ' + word + ' располагается до слова ' + word2)
elif word > word2:
    print('Cлово ' + word + ' располагается после слова ' + word2)
else:
    print('Шикарно, слова равны.')