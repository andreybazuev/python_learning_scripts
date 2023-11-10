#10.5_issorted принимает список в качестве параметра и возвращает True, если список отсортирован в порядке возрастания,
#и False в противном случае.

def is_sorted(t):
    ts = sorted(t)
    if t == ts:
        return True
    return False


#t = [1, 2, 3]
t = ["a", "b" , "c"]
print(is_sorted(t))