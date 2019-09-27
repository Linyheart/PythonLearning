import turtle
p = turtle.Turtle()
p.hideturtle()
turtle.bgcolor("darkgrey")
p.width(2)
colors = ["pink", "lightyellow", "lightgreen", "lightblue"]
turtle.tracer(False)
for i in range(1000):
    p.forward(2*i)
    p.color(colors[i % 4])
    p.left(91)
turtle.tracer(True)
turtle.done()
