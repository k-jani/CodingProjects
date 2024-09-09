import random
import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time


print("Start")

grph = 25
grph += 1
mygrph = np.zeros((grph, grph, 1), dtype = "uint8")

def UnOptDLA(size, itr):
    size += 1
    img = np.zeros((size, size, 1), dtype = "uint8")

    #Initalizer
    for col in range(0,size):
        img[size-1, col] = 1

    #Checks for all neighbhors excluding those above since they are not necessarily needed. 
    def notStk(row, col):
        cor = [row, col]
        unchkd = [[0,-1], [1,-1], [1,0], [0,1], [1,1]] #[-1,-1], [-1,0], [-1,1], 
        while (len(unchkd) > 0):
            transCor = unchkd[0]
            newCor = [cor[i] + transCor[i] for i in range(len(cor))]
            try:
                if img[newCor[0], newCor[1]] == 1:
                    return False
                else:
                    unchkd.remove(transCor)
                    continue
            except IndexError:
                unchkd.remove(transCor)
        return True

    strt = time.time()
    for i in range(itr):
        col = random.randint(0, size-1)
        row = 0
        while notStk(row, col):
            row += 1
        img[row, col] = 1
    return time.time() - strt

def OptDLA(size, itr):
    size += 1
    img = np.zeros((size, size, 1), dtype = "uint8")
    highPt = size - 1

    #Initalizer
    for col in range(0,size):
        img[size-1, col] = 1

    #Checks for all neighbhors excluding those above since they are not necessarily needed. 
    def notStk(row, col):
        cor = [row, col]
        unchkd = [[0,-1], [1,-1], [1,0], [0,1], [1,1]] #[-1,-1], [-1,0], [-1,1], 
        while (len(unchkd) > 0):
            transCor = unchkd[0]
            newCor = [cor[i] + transCor[i] for i in range(len(cor))]
            try:
                if img[newCor[0], newCor[1]] == 1:
                    return False
                else:
                    unchkd.remove(transCor)
                    continue
            except IndexError:
                unchkd.remove(transCor)
        return True

    strt = time.time()
    for i in range(itr):
        col = random.randint(0, size-1)
        row = 0
        while row <= highPt - 2:
            row += 1
        while notStk(row, col):
            row += 1
        if highPt > row:
            highPt = row
        img[row, col] = 1
    return time.time()-strt
    

for row in range(0, grph):
    for col in range(0, grph):
        size = (col+1) * 20
        itr = (row + 1) * 500
        mygrph[row, col] = UnOptDLA(size, itr) - OptDLA(size, itr)
        print(row, col, mygrph[row, col])

plt.imshow(mygrph), plt.show()
print("Finished.")
