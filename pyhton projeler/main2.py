import turtle

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

codeworld = turtle.Pen()

turtle.bgcolor('black')

for x in range(360):
    codeworld.pencolor(colors[x%6])
    codeworld.width(x//100+1)
    codeworld.forward(x)
    codeworld.left(59)
