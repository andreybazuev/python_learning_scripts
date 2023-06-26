def count(string, letter):
    count = 0
    for lettter in string:
        if lettter == 'а':
            count = count + 1
    print('буква', letter, count, 'раз(а) повторяется в слове')

string = input('введите строку: ')
letter = input('введите букву: ')

count(string, letter)