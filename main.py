import pygame
from player import *

pygame.init()
pygame.display.set_caption("Carnes Caindo Brutalmente")

screen = pygame.display.set_mode((800, 450))
clock = pygame.time.Clock()

background = pygame.image.load("images/cozinha.jpg")
background = pygame.transform.scale(background, (800, 450))

luffy = Player("images/luffy.png", {
    "left": pygame.K_a,
    "right": pygame.K_d
}, screen)

running = True

while running:

    screen.blit(background, (0, 0))

    luffy.render()
    luffy.move()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

    pygame.display.update()
    clock.tick(60)