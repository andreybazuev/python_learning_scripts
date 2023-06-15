# Отрисовка круга по его радиусу
import turtle

def circle (tur, npixels):
    
    angle = 360/npixels  # расчет угла
    for i in range (npixels): #для каждого из (количество отрезков)
        tur.fd(1)       # cсдвиг на 1 пиксель
        tur.rt(angle)   #сдвиг угла (tur.lt - в лево)
    

r = 100         # радиус круга
npixels = int (2 * 3.141592653589793 * r) # длина окружности в пикселях (количество отрезков)
bob = turtle.Turtle()

circle (bob, npixels)

