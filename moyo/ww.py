import turtle
import time

win = turtle.Screen()

turtle.register_shape("ee", ((4, 4), (4, -4), (-4, -4), (-4, 4)))

pen = turtle.Turtle()
pen.up()
x = -7
y = 5
pen.goto(x, y)
pen.color("green")
pen.shape("ee")
pen.speed(0)


pole = turtle.Turtle()

pole.penup()
pole.hideturtle()
pole.speed(0)
pole.width(4)
pole.goto(-102, 102)
pole.pendown()

for i in range(4):
    pole.fd(202)
    pole.right(90)

for t in range(20):
    pole.width(1)
    e = pole.xcor()
    e += 10
    pole.setx(e)
    pole.setheading(270)
    pole.fd(200)
    pole.sety(102)

pole.goto(100, 100)
x = pole.xcor()
for o in range(20):
    y = pole.ycor()
    pole.sety(y - 10)
    pole.setheading(180)
    pole.fd(200)
    pole.setx(x)

w = 0
qqq = True


while qqq:
    time.sleep(0.7)
    pen.up()
    stamp = pen.stamp()
    d = pen.xcor()
    pen.setx(d + 10)
    if w % 2 == 0:
        pen.clearstamps(1)
        w += 2
        print(1)

    else:
        w += 1



win.listen()
win.mainloop()
