from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()

        self.color("white")
        self.turtlesize(20, 100)
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)


    def up(self):
        # self.seth(90)
        # self.forward(20)
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)





