from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, pos=None) -> None:
        self.paddle=Turtle()
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(3,0.5)
        self.paddle.penup()
        self.paddle.goto(pos)
        self.the_field()
    
    def go_up(self):
        x,y=self.paddle.position()
        if y<265:
            self.paddle.goto(x,y+20)

    def go_down(self):
        x,y=self.paddle.position()
        if y>-260:
            self.paddle.goto(x,y-20)

    def the_field(self):
        for i in range(1,20):
            t=Turtle()
            t.shape("square")
            if i%2==0:
                t.color("white")
            else:
                t.color("black")
            t.shapesize(2, 0.2)
            t.penup()
            t.goto(0,-400+(i*40))
