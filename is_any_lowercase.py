#проверяет, есть ли в выражении заглавные буквы

def any_lowercase1(s):
    for c in s:
        print(c)
        if c.islower():
            continue
        else:
            return('эта буква заглавная!')
    return('все буквы прописные!')

print(any_lowercase1('мохИто'))