#выведет из файла слова без буквы "е" и посчитает их процент от общего количества

fin = open('words.txt')

without_e = 0
with_e = 0
for line in fin:
    word = line.strip()
    if 'e' not in word: 
        without_e += 1
        print(word)
    else:
        with_e +=1
print('слов всего:', without_e + with_e)
print('слов без буквы е:', without_e)
print('% от общего количества:', (round((without_e * 100) / (without_e + with_e),2)))