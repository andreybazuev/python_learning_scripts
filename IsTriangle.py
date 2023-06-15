def is_triangle(a, b, c):
    long = a
    
    if b > long:
        long = b
        short1 = a
        if c > long:
            long = c
            short2 = b
        else:
            short2 = c
    else:
        short1 = b
        if c > long:
            long = c
            short2 = a
        else:
            short2 = c
    
    

    if long < short1 + short2:
        print("Треугольник!")
    else: 
        print("Не треугольник!")
    return

a = int(input("введите длину первого отрезка:\n")) 
b = int(input("введите длину второго отрезка:\n")) 
c = int(input("введите длину третьего отрезка:\n"))

is_triangle(a, b, c)

#решение от ChatGPT
if a + b > c and a + c > b and b + c > a:
    print("Треугольник можно сложить")
else:
    print("Треугольник нельзя сложить")


