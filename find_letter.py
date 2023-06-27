def find(word, letter, ix): # ix - с какого индекса начинать поиск!
    index = ix
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return ">>>The letter is not in the word!"

print(find('abcdefg', 'd', 4))
