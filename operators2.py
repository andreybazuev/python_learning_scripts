#найдет буквы в первом слове, которые встречаются во втором слове
def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)

in_both('абрикос', 'апельсин')