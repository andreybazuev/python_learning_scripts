
# удваивает цифры в списке
def double_list(t):
    for i in range(len(t)):
        t[i] = t[i] * 2
    return t

#складывает все числа списка и выводит результат
def add_all(t):
    total = 0
    for x in t:
        total += x
    return total

#сортирует значения в списке
def sort(t):
    t.sort()
    return t


t = [42, 123, 15]
print(sort(t))