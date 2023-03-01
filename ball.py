from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        # self.shapesize(20, 20)

        self.x = random.randint(0, 350)
        self.y = random.randint(0, 350)
        self.penup()
        self.shape("circle")
        self.color("red")

        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce_y(self):
        self.y_move = self.y_move * -1

    def bounce_x(self):
        self.x_move = self.x_move * -1
        self.move_speed *= 0.05

    def reset_ballpos(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_move = self.x_move * -1

