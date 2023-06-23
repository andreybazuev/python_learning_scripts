"""Бряк, Вряк, Квяк, Кряк, Ляк, Мяк, Няк, Шмяк
конкатенация префиксов и суфиксов по условию"""

prefixes = 'БВККЛМНШ'
suffix1 = 'ряк'
suffixK = 'вяк'
suffix3 = 'як'
suffix4 = 'мяк'

for letter in prefixes:
    if letter == "Б" or letter == "В":
        print(letter + suffix1)

    elif letter == "К":
        print(letter + suffixK)
        suffixK = suffix1

    elif letter == "Л" or letter == "М" or letter == "Н":
        print(letter + suffix3)

    elif letter == "Ш":
        print(letter + suffix4)
        
    

    