#поиск всех индексов искомой буквы в строке


def find(word, letter): # ix - с какого индекса начинать поиск!
    index = 0
    print ('Длина слова в символах:', len(word))
    while index < len(word):
        if word[index] == letter:
            print('буква встречается в индексе:', index)
        index += 1


find('аврора', 'р')
