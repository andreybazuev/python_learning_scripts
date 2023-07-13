#строка из файла txt в список с разбивкой по словам
def txt_to_list(file):
    t = file.split() #сразу создает список по разделителю пробел

    return t

file = open("words.txt")    
print (txt_to_list(file.read()))


