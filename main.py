from turtle import Screen
from paddle import Paddle
from the_ball import Ball
from hit_wall import HitWall
import time



screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("PONG GAME.")
screen.tracer(0)


r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()


screen.listen()
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")

screen.onkeypress(l_paddle.go_up,"w")
screen.onkeypress(l_paddle.go_down,"s")

game_over=False
while not game_over:
    screen.update()
    time.sleep(0.1)
    ball.move()
    x,y=ball.ballTurtle.position()
    if y>300 or y<-300:
        ball.bounce()
    if x==340:
        if abs(r_paddle.paddle.position()[1] - y)<50:
            print(x,y," - ", r_paddle.paddle.position()[0],r_paddle.paddle.position()[1],l_paddle.paddle.position()[0],l_paddle.paddle.position()[1])
            ball.paddle_bounce()    
    if x==-340:
        if abs(l_paddle.paddle.position()[1] - y)<50:
            print(x,y," - ", r_paddle.paddle.position()[0],r_paddle.paddle.position()[1],l_paddle.paddle.position()[0],l_paddle.paddle.position()[1])
            ball.paddle_bounce()
    if x>380 or x<-380:
        print("GAME OVER")
        print(x,y," - ", r_paddle.paddle.position()[0],r_paddle.paddle.position()[1],l_paddle.paddle.position()[0],l_paddle.paddle.position()[1])
        exit()
screen.exitonclick()
