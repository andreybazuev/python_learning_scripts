#проверяет, имются ли в введенном списке повторяющиеся элементы
def has_duplicates(list1):

    t = sorted(list1) #при сортировке повт. элементы встанут рядом
    print (t)
    n = ''
    for i in t:  # тогда и проверим, есть ли повторы
        if i == n:
            return True
        else:
            n = i
    return False

list1 = ['a', 'f', 's', 'w', 'b']
print(has_duplicates(list1))



