#выведет из файла слова содержащие все символы из списка


def uses_all(vowel_letters):
    fin = open('words.txt')

    lenll = len(vowel_letters) #длина списка символов
    with_vowel = 0              #счетчик слов с всеми символами

    for line in fin:  
        word = line.strip() 
        count1 = 0                #счетчик пройденных символов в списке
        for letter in vowel_letters:           
            if letter not in word: 
                break
            else:
                count1 += 1
                if count1 == lenll: # если все символы пройдены
                    print(word)
                    with_vowel += 1
                continue

    print('всего слов с символами из списка:', with_vowel)

vowel_letters = 'aeiouy'
uses_all(vowel_letters)