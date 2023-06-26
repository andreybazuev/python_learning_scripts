#operators

word = 'Банан'
print (word.upper()) #строку в прописной регистр
print (word.lower()) #строку в строчный регистр
print (word.find('а')) #найти символ
print (word.find('на')) #найти подстроку
print (word.find('ан', 3)) #начать поиск с индекса 3
print (word.find('н', 0, 2)) # 'н' не встречается в диаппазоне от 0 до 2, выдаст -1

print('а' in word) #выдает True/False, если 'а' в(не в) слове


