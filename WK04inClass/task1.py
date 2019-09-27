import turtle
p = turtle.Turtle()
p.hideturtle()
turtle.bgcolor("darkgrey")
p.width(3)
colors = ["pink", "lightyellow", "lightgreen", "lightblue"]
# turtle.tracer(False)
for i in range(700):
    turtle.forward(2*i)
    turtle.color(colors[i % 4])
    turtle.left(91)
turtle.tracer(True)
turtle.done()
