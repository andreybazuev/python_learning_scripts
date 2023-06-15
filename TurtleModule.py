import turtle

def square (tur, length):
    for i in range(4):
        tur.fd(length)
        tur.lt(90)

length = 200
bob = turtle.Turtle()

square (bob, length)