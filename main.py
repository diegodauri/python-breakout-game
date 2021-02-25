from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

POSITION = [
    (-350, 250), (-300, 250), (-250, 250), (-200, 250), (-150, 250), (-100, 250), (-50, 250), (0, 250), (350, 250),
    (300, 250), (250, 250), (200, 250), (150, 250), (100, 250), (50, 250),
    (-350, 220), (-300, 220), (-250, 220), (-200, 220), (-150, 220), (-100, 220), (-50, 220), (0, 220), (350, 220),
    (300, 220), (250, 220), (200, 220), (150, 220), (100, 220), (50, 220),
    (-350, 190), (-300, 190), (-250, 190), (-200, 190), (-150, 190), (-100, 190), (-50, 190), (0, 190), (350, 190),
    (300, 190), (250, 190), (200, 190), (150, 190), (100, 190), (50, 190)]


obstacles = []
life = 3

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("breakout")
screen.tracer(0)

for position in POSITION:
    obstacle = Turtle()
    obstacle.goto(position[0], position[1])
    obstacle.color("white")
    obstacle.shape("square")
    obstacle.shapesize(stretch_wid=1, stretch_len=2)
    obstacles.append(obstacle)

paddle = Paddle((0, -270))
ball = Ball()
scoreboard = Scoreboard()
screen.update()

screen.listen()
screen.onkey(key="Right", fun=paddle.go_right)
screen.onkey(key="Left", fun=paddle.go_left)

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 380:
        ball.bounce_x()

    if ball.xcor() < -380:
        ball.bounce_x()

    if ball.ycor() < -280:
        life -= 1
        ball.reset_position()

    if ball.distance(paddle) < 50 and ball.ycor() > -340:
        ball.bounce_y()

    for obstacle in obstacles:
        if ball.distance(obstacle) < 50:
            scoreboard.point()
            index = obstacles.index(obstacle)
            obstacles.pop(index)
            ball.bounce_y()
            obstacle.reset()

    if len(obstacles) == 0:
        ball.reset()
        paddle.reset()
        text = Turtle()
        text.color("white")
        text.penup()
        text.hideturtle()
        text.goto(0, 0)
        text.write(f"You win\nLives remaning: {life}", align="center", font=("Courier", 30, "normal"))
        game_is_on = False

    if life == 0:
        ball.reset()
        paddle.reset()
        text = Turtle()
        text.color("white")
        text.penup()
        text.hideturtle()
        text.goto(0, 0)
        text.write(f"You lose\nBlocks remaining: {len(obstacles)}", align="center", font=("Courier", 30, "normal"))
        game_is_on = False



screen.exitonclick()