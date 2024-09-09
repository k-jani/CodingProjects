import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Test")

# Lines to make bounding box
ld = turtle.Turtle()
ld.color("white")
ld.speed(0)
ld.penup()
ld.goto(300, -310)
ld.pendown()
ld.goto(-300, -310)
ld.goto(-300, 100)
ld.penup()
ld.goto(300, 100)
ld.pendown()
ld.goto(300, -310)
ld.pendown()
ld.penup()
ld.goto(1000, 1000)
ld.color("black")

ball = turtle.Turtle()
ball.shape("circle")
ball.color("green")
ball.penup()
ball.speed(0)
ball.goto(0, 200)
#ball.dy = -2 #Velocity

ball.dy = random.randint(-2, 0)
ball.dx = random.randint(-1, 1)
if ball.dx == 0:
    tempvar = random.randint(1,2)
    if tempvar == 1:
        ball.dx = 1
    else:
        ball.dx = -1
    

G = .2
end = False


while True:
    
    while not end:

        ball.sety(ball.ycor() + ball.dy)
        ball.setx(ball.xcor() + ball.dx)
        ball.dy -= G #Acceleration and Gravity
        if ball.ycor() <= -300 and ball.dy < 0:

            ball.dy *= -1
            ball.dy *= .75
            ball.goto(ball.xcor(), -300)
        if ((ball.dy < 0.2 and ball.dy > 0) or (ball.dy > -.2 and ball.dy < 0)) and (ball.ycor() > -300 and ball.ycor() < -297):
            ball.dy = 0
            G = 0
            ball.goto(ball.xcor(), -300)
            end = True
        if ball.xcor() <= -290 and ball.dx < 0:

            ball.dx *= -1
            ball.dx *= .75
        if ball.xcor() >= 290 and ball.dx > 0:

            ball.dx *= -1
            ball.dx *= .75

        print(f"{ball.dy}, {ball.dx}")

    ball.dy = -2
    ball.goto(0, 200)
    end = False
    G = .2


wn.mainloop()
