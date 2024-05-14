import pygame
from random import randint, randrange, choice
from os import listdir

class Item:

    def __init__(self, screen):

        self.screen = screen
    
        # Decide aleatoriamente o tipo do item
        if randint(0, 1) > 0:

            # Akuma No Mi

            self.status = "bomb"
            self.image = pygame.image.load("images/akumanomi/"+choice(listdir("images/akumanomi")))

        else:

            # Comida

            self.status = "food"
            self.image = pygame.image.load("images/comidas/"+choice(listdir("images/comidas")))

        self.image = pygame.transform.scale(self.image, (64, 64))

        self.mask = pygame.mask.from_surface(self.image)

        # Eixo X aleatório
        self.pos_x = randint(0, self.screen.get_width() - self.image.get_width())

        self.pos_y = - self.image.get_height()

        # Velocidade aleatória
        self.velocity = randrange(1, 4)


    def render(self):

        self.screen.blit(self.image, (self.pos_x, self.pos_y))

    def fall(self):

        # Move o Item para baixo no Eixo Y
        self.pos_y += self.velocity