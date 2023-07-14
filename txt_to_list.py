spisok =  open("words2.txt").read().split()


for i in range(len(spisok)):
    word1 = spisok[i]
    for i in range(i + 1, len(spisok)):
        word2 = spisok[i]
        print (word1, word2)