import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time


print("Start")
size = 75
itr = 11017#200#11017
#Img setup
img = np.zeros((size, size, 1), dtype = "uint8")


antCor = [int(size/2), int(size/2)]

antDir = 0 #0 -> N, 1 -> E, etc...

for i in range(itr):

    #Turning based on 0 or 1, where 0 is left
    if not img[antCor[0]%size, antCor[1]%size]:
        antDir = (antDir + 1) % 4
    else:
        antDir = (antDir - 1) % 4
    
    #Setting current pos to inverted val        
    img[antCor[0]%size, antCor[1]%size] = int(not img[antCor[0]%size, antCor[1]%size])


    #Turn handler
    if antDir == 0:
        transCor = [0, -1]
    elif antDir == 1:
        transCor = [1, 0]
    elif antDir == 2:
        transCor = [0, 1]
    else:
        transCor = [-1, 0]
    antCor = [antCor[i] + transCor[i] for i in range(len(antCor))]
    

plt.imshow(img), plt.show()
print("Finished.")
