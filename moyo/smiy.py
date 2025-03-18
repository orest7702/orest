import turtle

win = turtle.Screen()
win.setup(width=700, height=700)
win.bgcolor()
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.width(9)
pen.color('black')
pen.up()
pen.goto(-100, 300)
pen.down()
pen.goto(-100, -300)
pen.up()
pen.goto(100, 300)
pen.down()
pen.goto(100, -300)
pen.up()
pen.goto(-300, 100)
pen.down()
pen.goto(300, 100)
pen.up()
pen.goto(-300, -100)
pen.down()
pen.goto(300, -100)
pen.up()
pen.goto(300, 300)
pen.down()
pen.goto(300, -300)
pen.goto(-300, -300)
pen.goto(-300, 300)
pen.goto(300, 300)
pen.up()


one = turtle.Turtle()
one.color('blue')
one.shape('square')
one.shapesize(stretch_wid=9.5, stretch_len=9.5)
one.pu()
one.goto(-200, 200)


two = turtle.Turtle()
two.color('yellow')
two.shape('square')
two.shapesize(stretch_wid=9.5, stretch_len=9.5)
two.pu()
two.goto(0, 200)


three = turtle.Turtle()
three.color('blue')
three.shape('square')
three.shapesize(stretch_wid=9.5, stretch_len=9.5)
three.pu()
three.goto(200, 200)


four = turtle.Turtle()
four.color('yellow')
four.shape('square')
four.shapesize(stretch_wid=9.5, stretch_len=9.5)
four.pu()
four.goto(-200, 0)


five = turtle.Turtle()
five.color('blue')
five.shape('square')
five.shapesize(stretch_wid=9.5, stretch_len=9.5)
five.pu()
five.goto(0, 0)


six = turtle.Turtle()
six.color('yellow')
six.shape('square')
six.shapesize(stretch_wid=9.5, stretch_len=9.5)
six.pu()
six.goto(200, 0)


seven = turtle.Turtle()
seven.color('blue')
seven.shape('square')
seven.shapesize(stretch_wid=9.5, stretch_len=9.5)
seven.pu()
seven.goto(-200, -200)


eight = turtle.Turtle()
eight.color('yellow')
eight.shape('square')
eight.shapesize(stretch_wid=9.5, stretch_len=9.5)
eight.pu()
eight.goto(0, -200)


nine = turtle.Turtle()
nine.color('blue')
nine.shape('square')
nine.shapesize(stretch_wid=9.5, stretch_len=9.5)
nine.pu()
nine.goto(200, -200)


def cross_cross(x, y,):
    pen.goto(x, y)
    pen.goto(x - 80, y + 80)
    pen.down()
    pen.goto(x + 80, y - 80)
    pen.up()
    pen.goto(x + 80, y + 80)
    pen.down()
    pen.goto(x - 80, y - 80)
    pen.up()


def zero_zero(x, y):
    pen.goto(x - 80, y + 80)
    pen.down()
    pen.goto(x + 80, y + 80)
    pen.goto(x + 80, y - 80)
    pen.goto(x - 80, y - 80)
    pen.goto(x - 80, y + 80)
    pen.up()


def zero(x, y):
    if x >= one.xcor()-95 and x <= one.xcor()+95 \
            and y >= one.ycor()-95 and y <= one.ycor()+95 :
        zero_zero(one.xcor(), one.ycor())

    elif x >= two.xcor()-95 and x <= two.xcor()+95 \
            and y >= two.ycor()-95 and y <= two.ycor()+95 :
        zero_zero(two.xcor(), two.ycor())

    elif x >= three.xcor()-95 and x <= three.xcor()+95 \
            and y >= three.ycor()-95 and y <= three.ycor()+95 :
        zero_zero(three.xcor(), three.ycor())

    elif x >= four.xcor()-95 and x <= four.xcor()+95 \
            and y >= four.ycor()-95 and y <= four.ycor()+95 :
        zero_zero(four.xcor(), four.ycor())

    elif x >= five.xcor()-95 and x <= five.xcor()+95 \
            and y >= five.ycor()-95 and y <= five.ycor()+95 :
        zero_zero(five.xcor(), five.ycor())

    elif x >= six.xcor()-95 and x <= six.xcor()+95 \
            and y >= six.ycor()-95 and y <= six.ycor()+95 :
        zero_zero(six.xcor(), six.ycor())

    elif x >= seven.xcor()-95 and x <= seven.xcor()+95 \
            and y >= seven.ycor()-95 and y <= seven.ycor()+95 :
        zero_zero(seven.xcor(), seven.ycor())

    elif x >= eight.xcor()-95 and x <= eight.xcor()+95 \
           and y >= eight.ycor()-95 and y <= eight.ycor()+95 :
        zero_zero(eight.xcor(), eight.ycor())

    elif x >= nine.xcor()-95 and x <= nine.xcor()+95 \
            and y >= nine.ycor()-95 and y <= nine.ycor()+95:
        zero_zero(nine.xcor(), nine.ycor())


def cross(x, y):
    if x >= one.xcor()-95 and x <= one.xcor()+95 \
            and y >= one.ycor()-95 and y <= one.ycor()+95 :
        cross_cross(one.xcor(), one.ycor())

    elif x >= two.xcor()-95 and x <= two.xcor()+95 \
            and y >= two.ycor()-95 and y <= two.ycor()+95 :
        cross_cross(two.xcor(), two.ycor())

    elif x >= three.xcor()-95 and x <= three.xcor()+95 \
            and y >= three.ycor()-95 and y <= three.ycor()+95 :
        cross_cross(three.xcor(), three.ycor())

    elif x >= four.xcor()-95 and x <= four.xcor()+95 \
                and y >= four.ycor()-95 and y <= four.ycor()+95 :
            cross_cross(four.xcor(), four.ycor())

    elif x >= five.xcor()-95 and x <= five.xcor()+95 \
            and y >= five.ycor()-95 and y <= five.ycor()+95 :
        cross_cross(five.xcor(), five.ycor())

    elif x >= six.xcor()-95 and x <= six.xcor()+95 and y >= six.ycor()-95 and y <= six.ycor()+95 :
        cross_cross(six.xcor(), six.ycor())

    elif x >= seven.xcor()-95 and x <= seven.xcor()+95 \
            and y >= seven.ycor()-95 and y <= seven.ycor()+95 :
        cross_cross(seven.xcor(), seven.ycor())

    elif x >= eight.xcor()-95 and x <= eight.xcor()+95 \
            and y >= eight.ycor()-95 and y <= eight.ycor()+95 :
        cross_cross(eight.xcor(), eight.ycor())

    elif x >= nine.xcor()-95 and x <= nine.xcor()+95 \
            and y >= nine.ycor()-95 and y <= nine.ycor()+95:
        cross_cross(nine.xcor(), nine.ycor())


def Gap():
    win.bye()


win.onclick(cross, btn=1)
win.onclick(zero, btn=3)
win.onkey(Gap, ' ')


win.listen()
win.mainloop()
