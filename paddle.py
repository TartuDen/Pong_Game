from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, pos=None) -> None:
        self.paddle=Turtle()
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(3,0.5)
        self.paddle.penup()
        self.paddle.goto(pos)
    
    def right_go_up(self):
        x,y=self.paddle.position()
        if y<265:
            self.paddle.goto(x,y+20)

    def right_go_down(self):
        x,y=self.paddle.position()
        if y>-260:
            self.paddle.goto(x,y-20)
    
    def left_go_up(self):
        x,y=self.paddle.position()
        if y<265:
            self.paddle.goto(x,y+20)

    def left_go_down(self):
        x,y=self.paddle.position()
        if y>-260:
            self.paddle.goto(x,y-20)