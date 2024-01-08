# Import all elements of the turtle library:
from turtle import *
from random import randint
import math
def drawSquare(side):
    tee.begin_fill()
    for _ in range(4):
        tee.forward(side)
        tee.left(90)
    tee.end_fill()
def fractalSquare(side):
    if side == size/2**(depth-1):
        return 0
    tee.up()
    tee.backward(side/4)
    tee.right(90)
    tee.forward(side/4)
    tee.left(90)
    tee.down()
    for x in range(4):
        drawSquare(side/2)
        fractalSquare(side/2)
        tee.up()
        tee.forward(side+side/2)
        tee.down()
        tee.left(90)
    tee.up()
    tee.forward(side/4)
    tee.left(90)
    tee.forward(side/4)
    tee.right(90)
    tee.down()
        
        
        
        
        
tee = Turtle()
Screen().tracer(0)
tee.shape("turtle")
tee.width(2)
tee.pencolor("white")
tee.speed(0)
#tee.tracer(0)

# Set up the graphics window:
tee.fillcolor("white")
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
colormode(255)
depth = int(input("Enter the depth: "))
size = int(input("Enter the initial size: "))
drawSquare(size)
fractalSquare(size)
