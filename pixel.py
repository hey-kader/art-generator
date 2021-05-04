import pygame        
from random import randint

# define RGBY colors

red = (255, 0, 0)
blue = (0,  0, 255)
green = (0,  255, 0)
yellow = (255, 255, 0)

def randomShade():

    rand = randint(1, 4)    
    if rand == 1:
        return red
    if rand == 2:
        return green
    if rand == 3:
        return blue
    if rand == 4:
        return yellow 

# returns a 2d array of rows of pixels
# each stored as a (r, g, b) and a (x, y) tuple

def grid ():

    tilesheet = []
    row = []
    first = True
    for x in range (0,1024,1):
        y = 0
        for y in range (0,1024,1):
            tilesheet.append([randomShade(),  (x,y)])

    return tilesheet

def color_change (c1, c2):
    
    if c1 == red and c2 == red:
       return blue 
    if c1 == blue and c2 == blue:
       return yellow 
    if c1 == yellow and c2 == yellow:
       return green 
    if c1 == green and c2 == blue:
       return red 

# make sure no colors are touching each other
# in the 64x64 grid of pixels in our 512 pixel square

def draw_sheet (window, sheet):
    print (sheet)
    for s in sheet:
        print (s)
        pygame.draw.rect(window, s[0], (s[1][0], s[1][1], 8, 8), 0) 

def main ():

    pygame.init ()
    window = pygame.display.set_mode((512,512))
    window.fill((255, 255, 255))

    draw_sheet(window, grid())

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            else:
                pygame.display.flip()

if __name__ == '__main__':
    main ()
