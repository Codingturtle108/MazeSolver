import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from queue import Queue
from bfsolver import bfs
from PathConstructor import constructor
from pixelClass import pixel
Maze = cv.imread('TestMazes/tiny.png')
height,width,_= Maze.shape
for i in range(width):
    if sum(Maze[0][i])==255*3:
        start = (i,0)
for j in range(height):
    if sum(Maze[height-1][j])==255*3:
        target = (j,height-1)
print(start,target)
def Pixel_Array(height,width):
    PixArray = [[pixel(0, 0, Maze) for _ in range(width)] for _ in range(height)]
    # PixArray= [[pixel(0,0,Maze)]*width]*height
    for i in range(width):
        for j in range(height):
            PixArray[i][j]=pixel(i,j,Maze)
    for i in range(width):
        for j in range(height):
            if i-1>=0 :
                PixArray[i][j].neighbours[0]=PixArray[i-1][j]
            if i+1<width :
                PixArray[i][j].neighbours[1] = PixArray[i+1][j]
            if j-1>=0:
                PixArray[i][j].neighbours[2]= PixArray[i][j-1]
            if j+1 < height:
                PixArray[i][j].neighbours[3] = PixArray[i][j+1]
    return PixArray
Object_Array=Pixel_Array(height,width)
pix_queue =Queue()
pix_queue.put(Object_Array[3][0])
path = bfs(pix_queue,target)
if path is not None:
    constructor(path)
