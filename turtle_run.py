import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('Black')
t.pencolor('Blue')
a = 0
b = 0
while True:
    t.forward(a)
    t.right(b)
    a+=3
    b+=1
    if b ==210:
        break
    t.hideturtle()

turtle.done()
