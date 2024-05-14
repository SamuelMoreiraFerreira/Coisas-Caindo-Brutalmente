import pygame
from player import *
from item import *

pygame.init()
pygame.display.set_caption("Carnes Caindo Brutalmente")

screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()

background = pygame.image.load("images/cozinha.jpg")
background = pygame.transform.scale(background, (800, 500))

luffy = Player("images/luffy.png", {
    "left": pygame.K_a,
    "right": pygame.K_d
}, screen)

items = list()

running = True

while running:

    screen.blit(background, (0, 0))

    luffy.render()
    luffy.move()

    for item in items:

        # Será apagado da lista após sair da tela
        if item.pos_y >= screen.get_height() or luffy.check_colission(item):

            items.remove(item)

        else:

            item.render()
            item.fall()

    # Sempre terá 8 itens sendo renderizado
    if len(items) < 8:

        items.append(Item(screen))


    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

    pygame.display.update()
    clock.tick(60)