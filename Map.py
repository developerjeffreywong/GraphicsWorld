# the map class
# this keeps track of what is stored in the map

import pygame # need the pygame libraries
class Map:

    #Constructor
    #w: width
    #h: height
    #ws: width space
    #hs: height space
    def __init__(self, w, h, ws, hs):
        self.cols = w # columns
        self.rows= h
        self.col_space=ws
        self.row_space=hs

    # draw the map
    # we draw the map
    def draw(self, screen):
        # draw horizontal lines
        for row in range(1, self.rows):
            #(the screen, color, (0, row), (window height, row)
            pygame.draw.line(screen, [0,0,0], [0,row*self.row_space], [self.col_space*self.cols,row*self.row_space]) 

        # draw the vertical lines
        for col in range(1, self.cols):
            #(the screen, color, (col, 0), (col, window width)
            pygame.draw.line(screen, [0,0,0], [col*self.col_space, 0], [col*self.col_space,self.rows*self.row_space]) 
