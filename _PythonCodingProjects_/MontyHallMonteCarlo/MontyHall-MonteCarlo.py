import random
import turtle
import time

#Turtle setup
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Monty Hall w/ Monte Carlo")
size = 250

#Bounding Box Drawer
wn.tracer(3, 1)
ld = turtle.Turtle()
ld.color("white"), ld.speed(0), ld.penup(), ld.goto(-size,-size)
ld.pendown(), ld.goto(-size, size), ld.goto(-size,-size), ld.goto(size,-size)
wn.tracer(25, 1)



def graph(rate, i, size, color):
    drwr = turtle.Turtle()
    drwr.color(color), drwr.speed(0),drwr.penup(), drwr.goto(i+1-size, (rate*2*size)-size), drwr.dot(), drwr.goto(size*5, size*5)#drwr.goto(i+1-size, (rate*2*size)-size), drwr.dot(), drwr.penup
    
def shuffle():
    #Randomize Door Winners
        prizes = [True, False, False]
        doorPrizes = []
        for i in range(len(prizes)):
            doorPrizes.append(random.choice(prizes))
            prizes.remove(doorPrizes[i])

        return doorPrizes
    
    
def noSwitch(numRuns, size):
    wins = 0
    for j in range(numRuns):

        if random.choice(shuffle()):
            wins += 1

        if j % (numRuns/(2*size)) == 0: graph(wins/(j+1), j/(numRuns/(2*size)), size, "white")

    return wins

def bound(size, lineVal):
    wn.clearscreen()
    wn.bgcolor("black")
    wn.tracer(3, 1)
    ld = turtle.Turtle()
    ld.color("white"), ld.speed(0), ld.penup(), ld.goto(-size, lineVal), ld.pendown(), ld.goto(size, lineVal), ld.penup(), ld.goto(-size,-size), ld.pendown(), ld.goto(-size, size), ld.goto(-size,-size), ld.goto(size,-size)
    wn.tracer(100, 1) #First num sets speed of graphs following the initial graph   


def Switch(numRuns, size):
    wins = 0
    
    for j in range(numRuns):
        
        doorPrizes = shuffle()

        doorSlct = random.randint(0,2)
        elimDoor = []
        for i in range(len(doorPrizes)):
            if not doorPrizes[i] and i != doorSlct:
                elimDoor.append(i)

        elimDoor = random.choice(elimDoor)
        
        for k in range(len(doorPrizes)):
            if k != doorSlct and k != elimDoor:
                if doorPrizes[k]:
                    wins += 1

        if j % (numRuns/(2*size)) == 0: graph(wins/(j+1), j/(numRuns/(2*size)), size, "orange")

    return wins


k = 1
for i in range(k):
    print(noSwitch(250, size)/250)
    if i != k -1: bound(size, -size/3)

for i in range(k):
    print(Switch(250, size)/250)
    if i != k-1: bound(size, size/3)
 
wn.mainloop()
