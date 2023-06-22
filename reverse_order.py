def reverse_order(string):
    lenght = len(string)
    i = -1
    a = 0
    while a < lenght:
        print (string[i])
        a +=1
        i -=1

string = input("Введите строку: >")

reverse_order(string)
