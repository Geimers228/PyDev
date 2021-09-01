import pygame
import math
pygame.init()
pi = ('Pi = ' + str(math.pi))
e = ('E = ' + str(math.e))
f = ('F = 0,1,1,2,3,5,8,13...')
p = ('P = 1,2,5,12,29...')
l = ('L = 2,1,3,4,7,11,18,29...')
pl = ('P-L = 2,6,14,34,82...')
display = pygame.display.set_mode((800,600))
pygame.display.set_caption('Nums')
font = pygame.font.SysFont('None', 72)
pitxt = font.render(pi, 0, (0,255,0))
etxt = font.render(e, 0, (0,255,0))
ftxt = font.render(f, 0, (0,255,0))
ptxt = font.render(p, 0, (0,255,0))
ltxt = font.render(l, 0, (0,255,0))
pltxt = font.render(pl, 0, (0,255,0))
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    display.blit(pitxt, (0,0))
    display.blit(etxt, (0,40))
    display.blit(ftxt, (0,80))
    display.blit(ptxt, (0,120))
    display.blit(ltxt, (0,160))
    display.blit(pltxt, (0,200))
pygame.quit()
