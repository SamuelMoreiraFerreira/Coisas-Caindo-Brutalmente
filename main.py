import pygame

pygame.init()
pygame.display.set_caption("Coisas Caindo Brutalmente")

screen = pygame.display.set_mode((1080, 1920))
clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

    pygame.display.update()
    clock.tick(60)