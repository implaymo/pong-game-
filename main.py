from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

SLEEP_TIME = 0.08

# Screen setup
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
scoreboard.update_scoreboard()

screen.listen()
# Right paddle
screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")
# Left Paddle
screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    ball.move_right()
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle_right) < 60 and ball.xcor() > 320 or ball.distance(paddle_left) < 60 and ball.xcor() < -320:
        # Changes speed of the ball
        SLEEP_TIME -= 0.01
        if SLEEP_TIME < 0.02:
            SLEEP_TIME = 0.02
        ball.bounce_x()

    # Right paddle misses = Goal for left side
    if ball.xcor() > 380:
        # Resets ball sleep
        SLEEP_TIME = 0.08
        ball.reset_position()
        scoreboard.l_point()
    # Left paddle misses = Goal for right side
    if ball.xcor() < -380:
        # Resets ball speed
        SLEEP_TIME = 0.08
        ball.reset_position()
        scoreboard.r_point()

    time.sleep(SLEEP_TIME)

screen.exitonclick()