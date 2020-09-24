import pygame
from game import Game

pygame.init()



pygame.display.set_caption("     Commet fall Game")
screen = pygame.display.set_mode((1080,720)) # screeny ... chamalle x 
background = pygame.image.load('assets/bg.jpg')


game = Game()
#  player = Player()
running = True
while running:
    screen.blit(background, (0,-200)) # 0,0 ????
    screen.blit(game.player.image, game.player.rect)
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Evento final xbe")
            
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True 
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
