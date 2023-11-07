#10.1 nested_sum() берет список списков целых чисел
#и складывает элементы из всех вложенных списков

def nested_sum(t):
    s = 0
    for i in t:
        for a in i:
            s += a
    return s


t = [[1, 2], [3], [4, 5, 6]]

print (nested_sum(t))

