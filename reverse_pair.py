# проверяет, являются ли слова обратной парой (порядок букв обратен порядку в другом)

'''def reverse_pair(word1, word2):
    l1 = list(word1)
    l2 = list(word2)
    t2 = -1
    if len(l1) == len(l2):
        for i in l1:
            if i == l2[t2]:
                t2 -= 1
            else:
                return False
        print(word1, word2)
    return False  '''

def reverse_pair(word1, word2):
    l1 = list(word1)
    l2 = list(word2) 
    l2.reverse()
    
    #print(l1, l2)
    
    if l1 == l2:
        print (word1, word2)
    else:
        return False


spisok =  open("words.txt").read().split()


for i in range(len(spisok)):
    word1 = spisok[i]
    for i in range(i + 1, len(spisok)):
        word2 = spisok[i]
        if len(word1) == len(word2):
            reverse_pair(word1, word2)




        