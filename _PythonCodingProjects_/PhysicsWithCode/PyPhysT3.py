import turtle
import time
import random
import threading

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Test")

G = 6.6743 * (10 ** -11)


class b1:
    b = turtle.Turtle()
    b.color("red")
    b.speed(0)
    b.penup()
    b.goto(100,-100)
    b.shape("circle")
    mass = 5.0
    vy = -2.0
    vx = 2.0

    
class b2:
    b = turtle.Turtle()
    b.color("green")
    b.speed(0)
    b.penup()
    b.goto(250,-5)
    b.shape("circle")
    mass = 5.0
    vy = -2.0
    vx = -2.0

class b3:
    b = turtle.Turtle()
    b.color("white")
    b.speed(0)
    b.penup()
    b.goto(-100,100)
    b.shape("circle")
    mass = 5.0
    vy = 2.0
    vx = -2.0

class b4:
    b = turtle.Turtle()
    b.color("yellow")
    b.speed(0)
    b.penup()
    b.goto(100,100)
    b.shape("circle")
    mass = 5.0
    vy = 2.0
    vx = 2.0


ballarr = [b1, b2, b3, b4]
sTime = time.time()
cTime = 0.01

def massper(ballarr, notball, index1):

    index2 = ballarr.index(notball)
    massball = ballarr[index1].mass
    massnot = ballarr[index2].mass

    massperball = massball / (massball + massnot)

    return massperball

def updty(ballarr):
# ----- Y Mover ------------------------------------------------------------------------------ #
    for ball in ballarr:
        index1 = ballarr.index(ball)
        for notball in ballarr:
            if ballarr.index(notball) != index1:
                notball.vy += (ball.b.ycor() - notball.b.ycor()) * .00001 * ((massper(ballarr, notball, index1) * notball.mass) + ((1.0 - massper(ballarr, notball, index1)) * ball.mass))
                if index1 % 2 == 0:
                    ball.vy -= .00001 * ((massper(ballarr, notball, index1) * notball.mass) + ((1.0 - massper(ballarr, notball, index1)) * ball.mass))
    for ball in ballarr:
        ball.b.sety(ball.b.ycor() + ball.vy)
def updtx(ballarr):
# ----- X Mover ------------------------------------------------------------------------------ #
    for ball in ballarr:
        index1 = ballarr.index(ball)
        for notball in ballarr:
            if ballarr.index(notball) != index1:
                notball.vx += (ball.b.xcor() - notball.b.xcor()) * .00001 * ((massper(ballarr, notball, index1) * notball.mass) + ((1.0 - massper(ballarr, notball, index1)) * ball.mass))
                if index1 % 2 == 0:
                    ball.vx -= .00001 * ((massper(ballarr, notball, index1) * notball.mass) + ((1.0 - massper(ballarr, notball, index1)) * ball.mass))
    for ball in ballarr:
        ball.b.setx(ball.b.xcor() + ball.vx)

                


while True:
    try:
        wn.tracer(8, 0)
        cTime = time.time() - sTime
        updtx(ballarr)
        updty(ballarr)
                #print(f"{ballarr[0].vy}, {ballarr[1].vy}, {ballarr[2].vy}")
    except ZeroDivisionError:
        print("Divide by Zero Error")


wn.mainloop()



print('''if (cTime > 5.0) & (cTime < 6.0):
            ballarr[random.randint(0,3)].vy += random.randint(3,4) / (random.randint(50,200) * 1.0)
        elif (cTime > 6.0) & (cTime < 7.0):
            ballarr[random.randint(0,3)].vy -= random.randint(3,4) / (random.randint(50,200) * 1.0)
''') # Random time gives random boost
