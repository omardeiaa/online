import pygame
from network import Network
from player import Player

width = 700
heigth = 700
icon = pygame.image.load("sugar-cube.png")
win = pygame.display.set_mode((width, heigth))
pygame.display.set_caption("Ping Pong")
pygame.display.set_icon(icon)

clientNumber = 0

def Redraw_Windows(win, player, player2):
    win.fill((255, 255, 255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()

def main():
    run = True
    n = Network
    p = n.getP()
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        p2 = n.send(p)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        Redraw_Windows(win, p, p2)

main()

