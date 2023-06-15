import turtle

turtle.hideturtle()
turtle.tracer(0)
turtle.penup()
turtle.setposition(-600, 0)
turtle.pendown()

axiom = "F"
tempAx = ""
iterable = 5
logic = {
    'F': 'F-F+F-F'
}

for i in range(iterable):
    for j in axiom:
        if j in logic:
            tempAx += logic[j]
        else:
            tempAx += j
    axiom, tempAx = tempAx, ''

for k in axiom:
    if k == '+':
        turtle.right(120)
    elif k == '-':
        turtle.left(60)
    else:
        turtle.forward(5)

turtle.update()
turtle.mainloop()