import pygame
from player import *
from item import *

pygame.init()
pygame.display.set_caption("Carnes Caindo Brutalmente")

screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()

#region Background

background = pygame.image.load("images/cozinha.jpg")
background = pygame.transform.scale(background, (800, 500))

#endregion

#region Fonte

font = pygame.font.SysFont("Comic Sans", 35, True)
game_over_txt = font.render("Você perdeu!", True, (255, 0, 0))

#endregion

#region Música de Fundo

pygame.mixer.music.load("sounds/theme.mp3")
pygame.mixer.music.set_endevent(pygame.USEREVENT)
pygame.mixer.music.play()

#endregion

#region Carregando Sons

eat_sound = pygame.mixer.Sound("sounds/eat.mp3")

#endregion

luffy = Player("images/luffy.png", {
    "left": pygame.K_a,
    "right": pygame.K_d,
    "ultimate": pygame.K_SPACE
}, screen)

items = list()

lost = False

running = True

while running:

    if not lost:

        screen.blit(background, (0, 0))

        luffy.render()
        luffy.move()

        for item in items:

            # Será apagado da lista após sair da tela
            if item.pos_y >= screen.get_height():

                items.remove(item)

            elif luffy.check_colission(item):

                # Som de Comer
                eat_sound.play()

                #region Comida

                if item.status == "bom":
            
                    # Incrementar a pontuação caso for comida

                    luffy.points += 10

                    # Apaga da lista            
                    items.remove(item)

                #endregion

                #region Akuma no Mi
                    
                if item.status == "ruim":

                    # Encerrar o jogo caso for Akuma no Mi

                    lost = True

                    screen.fill((0, 0, 0))
                    screen.blit(game_over_txt, ((screen.get_width() - game_over_txt.get_width()) / 2, (screen.get_height() - game_over_txt.get_height()) / 2))

                    # Pausar a música de fundo
                    pygame.mixer.music.pause()

                    break

                #endregion

            else:

                item.render()
                item.fall()

        # Sempre terá 8 itens sendo renderizado
        if len(items) < 8:

            items.append(Item(screen))

        # Pontuação
        screen.blit(font.render(f'Pontuação: {luffy.points}', True, (255, 0, 0)), (0, 0))

    #region Quit

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        if event.type == pygame.KEYDOWN:

            # Ultimate limpará todos os itens da tela
            if event.key == luffy.keys["ultimate"]:

                if luffy.ultimate > 0:

                    luffy.ultimate -= 1

                    items.clear()
        
    #endregion

    #region Update

    pygame.display.update()
    clock.tick(60)

    #endregion