def check_fermat(a, b, c, n):
    if a**n + b**n != c**n:
        print("нет, это не работает!")
    else:
        print("не может быть, Ферма ошибся!")
    return

a = int(input ("введите значение a:\n"))
b = int(input ("введите значение b:\n"))
c = int(input ("введите значение c:\n"))
n = int(input ("введите значение n:\n"))

check_fermat(a, b, c, n)