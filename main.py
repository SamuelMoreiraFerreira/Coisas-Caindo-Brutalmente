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

font = pygame.font.SysFont("Castellar", 35)
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

                eat_sound.play()

                # Incrementar a pontuação caso for comida
                if item.status == "food":
            
                    luffy.points += 10

                    # Apaga da lista            
                    items.remove(item)

                # Encerrar o jogo caso for Akuma no Mi
                if item.status == "bomb":

                    lost = True

                    screen.fill((0, 0, 0))
                    screen.blit(game_over_txt, ((screen.get_width() - game_over_txt.get_width()) / 2, (screen.get_height() - game_over_txt.get_height()) / 2))

                    break

            else:

                item.render()
                item.fall()

        # Sempre terá 8 itens sendo renderizado
        if len(items) < 8:

            items.append(Item(screen))

        # Se usar a ultimate todos os itens irão sumir
        if luffy.use_ultimate():

            items.clear()

            luffy.ultimate -= 1

        # Pontuação
        screen.blit(font.render(f'Pontuação: {luffy.points}', True, (255, 0, 0)), (0, 0))

    #region Quit

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

    #endregion

    #region Update

    pygame.display.update()
    clock.tick(60)

    #endregion