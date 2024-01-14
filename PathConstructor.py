import cv2 as cv
def constructor(path):
    Maze_Solved = cv.imread('TestMazes/combo6k.png')
    cv.namedWindow('Maze_Solved', cv.WINDOW_NORMAL)
    for x,y in path:
        Maze_Solved[y, x] = [0, 0, 255]
    # cv.imwrite('Output bfs/combo6ksolved.png',Maze_Solved)
    cv.imshow('Maze_Solved', Maze_Solved)
    cv.waitKey(0)
