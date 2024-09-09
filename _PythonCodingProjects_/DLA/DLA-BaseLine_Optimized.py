import random
import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time


print("Start")
size = 500
size += 1
itr = 25000
#Img setup
img = np.zeros((size, size, 1), dtype = "uint8")
highPt = size-1 #Sets the boundary for notStk to begin (decreases times notStk runs)

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
print(time.time() - strt)


plt.imshow(img)
plt.show()
print("Finished.")
