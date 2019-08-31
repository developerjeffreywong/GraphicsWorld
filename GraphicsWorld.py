# Graphic World

# MIT LICENSE
# Copyright (c) 2016 Jeffrey Wong (contact@jeffreywong.ca)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import pygame # use pygame
import sys # for system calls
import Map # the map of our game
import Player # the player of our game

pygame.init()
# the width and height of our map
width = 10
height= 10

# the space for each square on our grid
square_width = 50
square_height= 50

# create our window
screen = pygame.display.set_mode([width*square_width, height*square_height])

# our game state
running = True

# create our Map
theMap = Map.Map(width, height, square_width, square_height)

# create our player
thePlayer = Player.Player(width/2, height/2, square_width, square_height, "player.png")
# our draw function
def draw():
    # white background
    screen.fill([255,255,255])
    # draw our map
    theMap.draw(screen)

    # draw our player
    thePlayer.draw(screen, theMap)

    # update our display
    pygame.display.flip()

# our main game loop
while running:
    
    # check our events
    # event: mouse motions, key press, etc.
    for event in pygame.event.get():
        #check to see if we clicked the x button
        #on the top right of the window
        if event.type == pygame.QUIT:
            running = False

        # check to see if key is pressed
        elif event.type == pygame.KEYDOWN:
            # check which key is pressed
            # d is pressed, move right
            if event.key == pygame.K_d:
                thePlayer.x = thePlayer.x + 1
            # q is pressed, quit the game
            elif event.key == pygame.K_q:
                running = False
                
    # draw our stuff
    draw()

# we are quitting our game
pygame.quit() # exit pygame
sys.exit() # exit to our system
