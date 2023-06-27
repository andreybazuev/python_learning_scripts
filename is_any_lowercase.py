def any_lowercase1(s):
    for c in s:
        print(c)
        if c.islower():
            continue
        else:
            return('False')
    return('True')

print(any_lowercase1('мохито'))