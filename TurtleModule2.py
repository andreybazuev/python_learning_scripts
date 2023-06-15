import turtle

def polygon (tur, length, n): # отрисовка правильного многостороннего многоугольника
    for i in range(n):
        tur.fd(length)
        tur.lt(360/n) # внешние углы n-стороннего правильного многоугольника равны 360/n градусов.

def circle (r, tur):
    lencircle = 2 * 3.141592653589793 * r



r = 40          # радиус круга
n = 360          # количество отрезков
length = 1      # длина отрезков
bob = turtle.Turtle()

# polygon (bob, length, n)
circle (r, bob)

