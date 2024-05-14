import pygame

pygame.init()
pygame.display.set_caption("Coisas Caindo Brutalmente")

screen = pygame.display.set_mode((800, 450))
clock = pygame.time.Clock()

background = pygame.image.load("images/cozinha.jpg")
background = pygame.transform.scale(background, (800, 450))

running = True

while running:

    screen.blit(background, (0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

    pygame.display.update()
    clock.tick(60)