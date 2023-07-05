
# удваивает цифры в списке
def double_list(t):
    for i in range(len(t)):
        t[i] = t[i] * 2
    return t

#складывает все числа списка и выводит результат или встроенную функ. sum(t)
def add_all(t):
    total = 0
    for x in t:
        total += x
    return total

#сортирует значения в списке
def sort(t):
    t.sort()
    return t

#Меняет первые буквы элементов списка на прописные
def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

#Возвращает элементы списка если они содержат только прописные буквы
def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res

#Удаляем элементы списка
def del_elems(t):
    x = t.pop(1) #метод pop возвращает удаляемый элемент
    del t[2]     #инструкция del только удаляет
    return t, x



t = ['Fc', 'ZE', 'we', 'yG']
print(del_elems(t))