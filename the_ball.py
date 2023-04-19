from turtle import Turtle
import random
import time

class Ball(Turtle):
    def __init__(self):
        self.ballTurtle=Turtle()
        self.ballTurtle.shape("square")
        self.ballTurtle.color("green")
        self.ballTurtle.penup()
        self.ballTurtle.goto(0,0)
        self.x_move=10
        self.y_move=10   
 

    def move(self):            
        x,y=self.ballTurtle.position()
        self.ballTurtle.goto(x+self.x_move,y+self.y_move)

    def bounce(self):
        self.y_move=-self.y_move
    
    def paddle_bounce(self):
        self.x_move=-self.x_move





