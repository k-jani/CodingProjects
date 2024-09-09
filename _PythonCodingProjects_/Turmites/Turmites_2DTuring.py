import numpy as np
#import cv2
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#import time
import random

print("Start.")
size = 155
try:
    itr = input("Enter a number like 10000: ")#11017
    itr = int(itr)
    for i in range(itr):
        break
except:
    print("Non-integer entered, itr auto set to 10000. ")
    itr = 10000


#Img setup
img = np.zeros((size, size, 1), dtype = "uint8")
antCor = [int(size/2), int(size/2)]
antDir = 0 #0 -> N, 1 -> E, etc...

ptrn = []#[1, 1, 1, 1, 1, 1, 1, 2, 1, 2] # 0-frwd, 1-L, 2-R, 3-U-trn
#10010 -- Binary
#2231233013110
#[1, 1, 1, 2, 2, 2, 2, 1] - Growth
def randPtrn(ptrn):
    for i in range(random.randint(3, 10)):
        ptrn.append(random.randint(0,3))#0, 3))
    print(ptrn)    

#randPtrn(ptrn)
ptrn = [3, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2]

def strtup(ptrn):
    newClr = []
    for i in range(len(ptrn)):
        newClr.append((i + len(ptrn) - 1) % len(ptrn))
    return newClr
 
def update(size, itr, img, antCor, antDir, ptrn):
    for i in range(itr):

        #Turning based on rules: 0-frwd, 1-L, 2-R, 3-U-trn
        if ptrn[int(img[antCor[0]%size, antCor[1]%size])] == 0:
            antDir = antDir
        elif ptrn[int(img[antCor[0]%size, antCor[1]%size])] == 1:
            antDir = (antDir + 1) % 4
        elif ptrn[int(img[antCor[0]%size, antCor[1]%size])] == 2:
            antDir = (antDir - 1) % 4
        else:
            antDir = (antDir - 2) % 4
            
        
        #Setting current pos to variety of vals       
        img[antCor[0]%size, antCor[1]%size] = strtup(ptrn)[int(img[antCor[0]%size, antCor[1]%size])]


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


update(size, itr, img, antCor, antDir, ptrn)
plt.imshow(img), plt.show()
print('''Finished.''')
