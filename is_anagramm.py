#проверяет, являются ли веденные слова анаграммой
def is_anagram(str1, srt2):

    t1 = sorted(list(str1))
    t2 = sorted(list(str2))
    print (t1)
    print (t2)

    if t1 == t2:
        return "Это анаграмма"
    else:
        return "Слова не являются анаграммой"



str1 = input('введите стр1:')    
str2 = input('введите стр2:') 
print(is_anagram(str1, str2))  