from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)

l_paddle = Paddle((-300, 0))
r_paddle = Paddle((300, 0))
ball = Ball()


screen.listen()
screen.onkeypress(l_paddle.up,"w")
screen.onkeypress(l_paddle.down,"s")

screen.onkeypress(r_paddle.up,"Up")
screen.onkeypress(r_paddle.down,"Down")


# screen.onkey(paddle2.up,"W")
# screen.onkey(paddle2.down,"S")
scoreboard = Scoreboard()
game_on = True
while game_on:
    sleep(ball.move_speed)
    ball.move()
    #print(f"before if {ball.xcor()}")
    if ball.ycor() > 270 or ball.ycor() < -270:
        #print(f"while loop {ball.xcor()} {ball.position()}")
        ball.bounce_y()

    if ball.distance(l_paddle) < 50 and ball.xcor() > -270 or ball.distance(r_paddle) < 50 and ball.xcor() < 270:
        ball.bounce_x()
        ball.speed(10)

    if ball.xcor() > 340:
        ball.reset_ballpos()
        scoreboard.l_point()

    if ball.xcor() < -340:
        ball.reset_ballpos()
        scoreboard.r_point()
        # screen.clearscreen()




    screen.update()

screen.exitonclick()