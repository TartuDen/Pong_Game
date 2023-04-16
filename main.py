from turtle import Turtle, Screen

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("PONG GAME.")
screen.tracer(0)


paddle=Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(3,0.5)
paddle.penup()
paddle.goto(350,0)
screen.update()

def go_up():
    
    x,y=paddle.position()
    print(x,y)
    paddle.goto(x,y+20)
    screen.update()

def go_down():
    
    x,y=paddle.position()
    print(x,y)
    paddle.goto(x,y-20)
    screen.update()


screen.listen()
screen.onkeypress(go_up,"Up")
screen.onkeypress(go_down,"Down")



screen.exitonclick()
