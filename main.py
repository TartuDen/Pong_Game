from turtle import Screen
from paddle import Paddle
from the_ball import Ball


screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("PONG GAME.")
screen.tracer(0)


r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()




def left_go_up():
    x,y=l_paddle.paddle.position()
    if y<265:
        l_paddle.paddle.goto(x,y+20)

def left_go_down():
    x,y=l_paddle.paddle.position()
    if y>-260:
        l_paddle.paddle.goto(x,y-20)

screen.listen()
screen.onkeypress(r_paddle.right_go_up,"Up")
screen.onkeypress(r_paddle.right_go_down,"Down")

screen.onkeypress(l_paddle.left_go_up,"w")
screen.onkeypress(l_paddle.left_go_down,"s")

game_over=False
while not game_over:
    screen.update()

screen.exitonclick()
