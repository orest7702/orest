import turtle

screen = turtle.Screen()
screen.bgcolor("#0c0413")
screen.setup(width=1.0, height=1.0)

pen = turtle.Turtle()
pen.speed(0)
pen.up()



pen.color("#000000")
pen.goto(-700, -200)
pen.begin_fill()
pen.goto(700, -200)
pen.goto(700, -370)
pen.goto(-700, -370)
pen.end_fill()


screen.mainloop()
