from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        self.ballTurtle=Turtle()
        self.ballTurtle.shape("square")
        self.ballTurtle.color("green")
        self.ballTurtle.penup()
        self.ballTurtle.goto(0,0)

