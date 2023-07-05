#Строка в список используя встроенную функцию list()
def str_to_list(s):
    t = list(s)
    return t

#строка в список разбивка по словам с помощью метода split()
def strw_to_list(s):
    t = s.split()
    return t

#строка в список разбивка по символам - разделителям (напр: тоска/по/фьордам')
def strd_to_list(s):
    delimiter = '/'
    t = s.split(delimiter)
    return t


s = 'тоска/по/фьордам'
print(strd_to_list(s))


