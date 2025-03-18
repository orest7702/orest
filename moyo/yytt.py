import turtle


win = turtle.Screen()
win.setup(1100, 400)
win.bgcolor("green")

pen = turtle.Turtle()
pen.shape("circle")
pen.speed(0)
pen.up()
pen.setpos(450, 0)
pen.down()


speed = 1
dd = True


def q(x, y):
    print(x, y)
    print(pen.distance(x, y))
    pen.speed(1)
    pen.goto(x,y)


pen.ondrag(q, 1)
win.onclick(q, 1)


win.listen()
win.mainloop()
