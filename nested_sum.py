#суммирует все числа во вложенных списках
def nested_sum(t):
    total = 0
    for i in t:
        for n in i:
            total += n
    return total

#выдает новый список с кумулятивной суммой
def cumsum(t):
    sum = 0
    csl = []
    for i in t:
        sum += i
        csl.append(sum)
    return csl


t = [1, 2, 3, 4, 5]  

print (cumsum(t))

