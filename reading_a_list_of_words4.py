#выведет из файла слова где буквы располагаются в алфавитном порядке



def is_abecedarian(source):

    fin = open(source)
    abc_words = 0 # будет общее кол-во слов в алф. порядке    
    for line in fin:  
        word = line.strip()
        pos = 0
        count1 = 0
        for letter in word:
            if ord(letter) < pos: #если числовой код символа меньше pos (пример b<a)
                break
            else:
                count1 += 1
                pos = ord(letter) #pos присвоить числовой код текущей буквы
                if count1 == len(word): # если все символы пройдены
                    print(word)
                    abc_words += 1
                continue

    print('всего слов с буквами в алфавитном прядке:', abc_words)

is_abecedarian('words.txt')




