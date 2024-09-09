import numpy as np
import cv2
import matplotlib.pyplot as plt
#from matplotlib.animation import FuncAnimation
from time import gmtime, strftime
import random

print("Start.")
size = 500
#Img setup
img = np.zeros((size, size, 1), dtype = "uint8")

img[-1, int(size/2)] = 1

#Converts rule into binary
print('''
|----------------------------|
Recommended Rules:
30
57
73
109
126
225
|----------------------------|

''')
rule = int(input("Ruleset (int btwn 0 and 255): "))
rule2 = rule
rule = [int(x) for x in bin(rule)[2:]]
while len(rule) != 8: rule.insert(0, 0)

#Neighbhor list:
groupList = [[1, 1, 1], [1, 1, 0], [1, 0, 1], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 0, 1], [0, 0, 0]]



for y in range(size):
    for x in range(size):
        img[y, x] = rule[groupList.index([int(img[y-1, x-1]), int(img[y-1, x]), int(img[y-1, (x+1) % size])])]



plt.imshow(img), plt.show()
min_val,max_val=img.min(),img.max()
img = 255.0*(img - min_val)/(max_val - min_val)
img = img.astype(np.uint8)
#cv2.imwrite(f"myRule{rule2}_{size}.tif", img)
#myTime = strftime("%a, %d %b %Y %H:%M:%S", gmtime())
#cv2.imwrite(f'myRule40{myTime}.tif', img)
print('''Finished.''')
