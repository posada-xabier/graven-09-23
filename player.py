import pygame

class Player(pygame.sprite.Sprite ):
    # sprite elemento en nuestra ventana de juego, puede moverse

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5 # pixel 5
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def move_right(self):
        self.rect.x += self.velocity
    def move_left(self):
        self.rect.x -= self.velocity 


