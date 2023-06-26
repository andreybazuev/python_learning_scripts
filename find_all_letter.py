#поиск всех индексов искомой буквы в строке


def find(word, letter):
    index = 0
    print ('Длина слова в символах:', len(word))
    while index < len(word):
        if word[index] == letter:
            print('символ встречается по индексу:', index)
        index += 1


find('аврора', 'р')
