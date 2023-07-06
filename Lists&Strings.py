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

#возврат строки, начиная со 2го слова.  
def tail(s):
    t = s.split()       #Сначала преобразуем в список,
    s1 = ' '.join(t[1:])    #затем обьединяем срез
    return s1

s = 'тоска по фиордам'
t = tail(s)
print(t)

#метод join() обьединяет список в строку. Вызывается для 
# разделителя и принимает список в качестве параметра.
'''delimiter = '@'
print (delimiter.join(t)) '''



