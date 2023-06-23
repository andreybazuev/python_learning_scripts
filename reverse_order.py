def reverse_order(string):
    lenght = len(string)
    i = -1
    while abs(i+1) < lenght:
        print (string[i])
        i -= 1

string = input("Введите строку: >")

reverse_order(string)


#используя цикл for
"""def reverse_order(string):
    lenght = len(string)
    i = -1
    for s in string:
        print (string[i])
        i -= 1

string = input("Введите строку: >")
reverse_order(string)"""