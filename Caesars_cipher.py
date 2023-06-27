#Шифр Цезаря сдвигает каждую букву word на значение shift

def rotate_word(word, shift):
    word1 = ''
    for i in word:
        i = chr(ord(i)+shift)
        print (i) 
        word1 += i
    return word1


print (rotate_word('EEE', 1))