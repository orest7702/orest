import turtle
from random import choice

win = turtle.Screen()
win.setup(width=1.0, height=1.0)
win.bgcolor('black')

pole = turtle.Turtle()
pole.color('green')
pole.hideturtle()
pole.speed(0)
pole.up()
pole.begin_fill()
pole.goto(-500, 300)
pole.down()
pole.goto(500, 300)
pole.goto(500, -300)
pole.goto(-500, -300)
pole.goto(-500, 300)
pole.end_fill()
pole.goto(0, 300)
pole.color('white')
pole.setheading(270)

for i in range(25):
    if i % 2 == 0:
        pole.down()
        pole.forward(24)

    else:
        pole.up()
        pole.forward(24)

racetca_1 = turtle.Turtle()
racetca_1.color('white')
racetca_1.shape('square')
racetca_1.shapesize(stretch_wid=5, stretch_len=1)
racetca_1.up()
racetca_1.goto(-450, 0)

racetca_2 = turtle.Turtle()
racetca_2.color('white')
racetca_2.shape('square')
racetca_2.shapesize(stretch_wid=5, stretch_len=1)
racetca_2.up()
racetca_2.goto(450, 0)


def up():
    y = racetca_1.ycor()
    x = racetca_1.xcor()
    if y >= 250:
        racetca_1.goto(x, 250)

    else:
        racetca_1.goto(x, y + 20)


def down():
    y = racetca_1.ycor()
    x = racetca_1.xcor()
    if y == -250:
        racetca_1.goto(x, -250)

    else:
        racetca_1.goto(x, y - 20)


def uup():
    y = racetca_2.ycor()
    x = racetca_2.xcor()
    if y >= 250:
        racetca_2.goto(x, 250)

    else:
        racetca_2.goto(x, y + 20)


def ddown():
    y = racetca_2.ycor()
    x = racetca_2.xcor()
    if y == -250:
        racetca_2.goto(x, -250)

    else:
        racetca_2.goto(x, y - 20)


win.onkeypress(up, 'w')
win.onkeypress(down, 's')

win.onkeypress(uup, 'Up')
win.onkeypress(ddown, 'Down')


win.listen()

ball = turtle.Turtle()
ball.shape('circle')
ball.speed(0)
ball.up()
ball.dx = 4
ball.dy = 4

while True:
    win.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() >= 290:
        ball.dy = -ball.dy

    if ball.ycor() <= -290:
        ball.dy = -ball.dy

    if ball.xcor() >= 490:
        ball.goto(0, 0)
        ball.dx = choice([-4, -3, -2, 2, 3, 4])
        ball.dy = choice([-4, -3, -2, 2, 3, 4])

    if ball.xcor() <= -490:
        ball.goto(0, 0)
        ball.dx = choice([-4, -3, -2, 2, 3, 4])
        ball.dy = choice([-4, -3, -2, 2, 3, 4])

    if ball.ycor() >= racetca_2.ycor()-50 and ball.ycor() <= racetca_2.ycor()+50 \
        and ball.xcor() >= racetca_2.xcor()-5 and ball.xcor() <= racetca_2.xcor()+5 :
        ball.dx = -ball.dx

    if ball.ycor() >= racetca_1.ycor() - 50 and ball.ycor() <= racetca_1.ycor() + 50 \
            and ball.xcor() >= racetca_1.xcor() - 5 and ball.xcor() <= racetca_1.xcor() + 5:
        ball.dx = -ball.dx


win.mainloop()
