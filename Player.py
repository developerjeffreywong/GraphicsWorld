# the player class
import pygame # we need pygame drawing stuff

class Player:

    # Constructor
    # x position
    # y position
    # w: width
    # h: height
    # i: image
    def __init__(self, x, y, w, h, i):
        self.x = x
        self.y = y
        self.width = w
        self.height= h
        self.image = pygame.image.load(i)

        # scale the image to the width and height we want
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    # draw
    # draw our player
    def draw(self, screen, theMap):
        screen.blit(self.image, [self.x*theMap.col_space, self.y * theMap.row_space])
