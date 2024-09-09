import matplotlib.pyplot as plt
import numpy as np
from numpy import random
import cv2

#Sets the size and the number of cells in the image
size = 100
numpts = 50

myimg = np.zeros((size,size), dtype='uint8')
myimg2 = np.zeros((size,size), dtype='uint8')


keypts=[[random.randint(0,size-1),random.randint(0,size-1)] for i in range(numpts)]

#Srching function which uses either pythagorean or manhattan distance depending on style val
def srch(keypts, xcor, ycor, style):
    #Finds the kypts pos of clst keypt
    clst = 0
    clst_dist = 2*size

    if style: #Manhattan dist when style = 1
        for cors in enumerate(keypts):

            if (abs(cors[1][0]-xcor) + abs(cors[1][1]-ycor)) < clst_dist: #Finds manhattan dist

                clst_dist = abs(cors[1][0]-xcor) + abs(cors[1][1]-ycor)
                clst = cors[0]
    else:  #Pythagorean dist when style != 1 
        for cors in enumerate(keypts):

            if (abs(cors[1][0]-xcor)**2 + abs(cors[1][1]-ycor)**2)**.5 < clst_dist: #Finds manhattan dist

                clst_dist = (abs(cors[1][0]-xcor)**2 + abs(cors[1][1]-ycor)**2)**.5
                clst = cors[0]

    return clst

def doVoronoi(size, myimg, keypts, style):
    for row in range(size):
        for col in range(size):
            myimg[row,col] = srch(keypts, row, col, style)

    for cors in enumerate(keypts):
        myimg[cors[1][0], cors[1][1]] = numpts+5 #Adds 5 to value of max to make keypts relatively bright

    return myimg


myimg = doVoronoi(size, myimg, keypts, 0) #pyth
myimg2 = doVoronoi(size, myimg2, keypts, 1) #manhat


plt.matshow(myimg)
plt.title("Pythagorean Dist")
plt.matshow(myimg2)
plt.title("Manhattan Dist")

plt.show()
