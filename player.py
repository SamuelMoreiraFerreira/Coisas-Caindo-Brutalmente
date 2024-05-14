import pygame

class Player:

    def __init__(self, image:str, keys:dict, screen):

        self.screen = screen

        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (128, 165))

        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.mask = pygame.mask.from_surface(self.image)

        # Dicionário com as teclas
        self.keys = keys

        # Posiciona ao meio do eixo X
        self.pos_x = (self.screen.get_width() - self.width) / 2
        self.pos_y = self.screen.get_height() - self.height

    def render(self):

        self.screen.blit(self.image, (self.pos_x, self.pos_y))

    def move(self, steps:int=5):

        pressed_keys = pygame.key.get_pressed()

        vet_x = pressed_keys[self.keys["left"]] - pressed_keys[self.keys["right"]]

        vet_x = self.pos_x - vet_x * steps 

        # Limita o movimento a borda das janelas
        if vet_x >= 0 and vet_x <= self.screen.get_width() - self.width:

            # Altera o eixo X do objeto
            self.pos_x = vet_x