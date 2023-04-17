from turtle import Turtle

class Ball(Turtle):
    def __init__(self, screen):
        self.ballTurtle=Turtle()
        self.ballTurtle.shape("square")
        self.ballTurtle.color("green")
        self.ballTurtle.penup()
        self.ballTurtle.goto(0,0)
        self.screen=screen

        self.step_x=800/100
        self.step_y=600/100
        self.screen.tracer(1)
        

    def ball_start(self):
        while self.ballTurtle.position()[0] < 400 and self.ballTurtle.position()[1] < 300:
            x,y=self.ballTurtle.position()
            self.ballTurtle.goto(x+self.step_x,y+self.step_y)

