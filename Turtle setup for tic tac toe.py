
import turtle

def draw_grid():
    turtle.home()
    for i in range(4):
        turtle.forward(240)
        turtle.right(90)
    for j in range(1, 3):
        turtle.pendown()
        turtle.forward(j*80)
        turtle.right(90)
        turtle.forward(240)
        turtle.penup()
        turtle.home()
    for k in range(1, 3):
        turtle.pendown()
        turtle.right(90)
        turtle.forward(k*80)
        turtle.left(90)
        turtle.forward(240)
        turtle.penup()
        turtle.home()

def goto_center(string):
    num = string[1]
    num = int(num)
    letter = string[0]
    forward = (80*num) - 40
    if letter == "A":
        i = 1
    elif letter == "B":
        i = 2
    else:
        i = 3
    forward_2 = (80*i) - 40
    turtle.home()
    turtle.setheading(0)
    turtle.penup()
    turtle.forward(forward)
    turtle.right(90)
    turtle.forward(forward_2)
        

def draw_cross():
    c_pos = turtle.pos()
    for m in range(1, 5):
        turtle.penup()
        turtle.goto(c_pos)
        turtle.setheading(0)
        turtle.pendown()
        turtle.left((90*m)-45)
        turtle.forward(30)
    turtle.penup()
    turtle.home()

def draw_circle():
    turtle.setheading(270)
    turtle.penup()
    turtle.forward(30)
    turtle.setheading(0)
    turtle.pendown()
    turtle.circle(30)
    turtle.penup()
    turtle.home()
    
draw_grid()
goto_center("B2")
draw_cross()
goto_center("C1")
draw_circle()







