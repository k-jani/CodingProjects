import turtle
import random
import time

 

class b1:
    b = turtle.Turtle()
    b.color("red")
    b.speed(0)
    b.penup()
    b.goto(-100,0)
    b.shape("circle")
    vy = 1.1
    vx = 1.1
    
class b2:
    b = turtle.Turtle()
    b.color("green")
    b.speed(0)
    b.penup()
    b.goto(100,50)
    b.shape("circle")
    vy = 2.1
    vx = 1.1

ballarr = [b1, b2]
strtT = time.time()
curT = time.time()-strtT



def updtvy(ballarr):

    for i in range(len(ballarr)-1):

        print(ballarr[i].vy)
        print(ballarr[i+1].vy)
        ballarr[i].vy += (ballarr[i+1].b.ycor() - ballarr[i].b.ycor()) * .01 #(1.0 / (((ballarr[i+1].b.ycor() - ballarr[i].b.ycor()) * 10))+.001)     (1.0/((ballarr[i+1].b.ycor() - ballarr[i].b.ycor()) + .001))
        #if ballarr[i+1].b.ycor() - ballarr[i].b.ycor() != 0.0:
        #    ballarr[i].vy += (ballarr[i+1].b.ycor() - ballarr[i].b.ycor()) #* (1.0/(ballarr[i+1].b.ycor() - ballarr[i].b.ycor())) #Where difference in y-val times
        #else:
        #    ballarr[i].vy += 0
    print("\n")



def updtvx(ballarr):

    for i in range(len(ballarr)-1):

        print(ballarr[i].vx)
        print(ballarr[i+1].vx)
        ballarr[i].vx += (ballarr[i+1].b.xcor() - ballarr[i].b.xcor()) * .01 #(1.0 / (((ballarr[i+1].b.ycor() - ballarr[i].b.ycor()) * 10))+.001)     (1.0/((ballarr[i+1].b.ycor() - ballarr[i].b.ycor()) + .001))
        #if ballarr[i+1].b.ycor() - ballarr[i].b.ycor() != 0.0:
        #    ballarr[i].vy += (ballarr[i+1].b.ycor() - ballarr[i].b.ycor()) #* (1.0/(ballarr[i+1].b.ycor() - ballarr[i].b.ycor())) #Where difference in y-val times
        #else:
        #    ballarr[i].vy += 0
    print("\n")


def updt(ballarr):

    updtvy(ballarr)
    updtvx(ballarr)
    
    for ball in ballarr:
        ball.b.sety(ball.b.ycor()+ball.vy)
        ball.b.setx(ball.b.xcor()+ball.vx)




   
strtT = time.time()
while True:
    updt(ballarr)
    curT = time.time()-strtT
    #print(curT)
    
wn.mainloop()


#for n in range(len(ballarr)):
#            if n == 1:
#                continue
#            else:
#                ballarr[i].vy += (ballarr[i+n].b.ycor())-(ballarr[i].b.ycor()) #To allow for 3 balls, make a for loop (going through length of ballarr and starting on pos 1 instead of 0) that has for "n" in and have i+1 become i+n


