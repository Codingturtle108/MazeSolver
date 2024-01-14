class pixel:
    def __init__(self, x, y,Img):
        self.cord = (x,y)
        self.parent = self
        self.visited = 0
        self.neighbours=[None,None,None,None]
        self.color =Img[y,x]

