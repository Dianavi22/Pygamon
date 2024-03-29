import pygame
import pytmx
import pyscroll

from player import Player


class Game:

    def __init__(self):

        #créer la fenêtre du jeu
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pygamon-aventure")

        #charger la carte (tmx)
        tmx_data = pytmx.util_pygame.load_pygame('carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        #générer un joueur
        player_position = tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x, player_position.y)

        #dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer = map_layer, default_layer=3)
        self.group.add(self.player)


    def run(self):

        #boucle du jeu
        running = True

        while running:

            self.group.update()
            self.group.center(self.player.rect)
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()