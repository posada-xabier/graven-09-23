import pygame
pygame.init()

pygame.display.set_caption("     Commet fall Game")
screen = pygame.display.set_mode((1080,720)) # screeny ... chamalle x 
background = pygame.image.load('assets/bg.jpg')

running = True
while running:
    screen.blit(background, (0,-200)) # 0,0 ????
    pygame.display.flip()
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Evento final, cierre click en x up-right window , Fermeture de fenetre") 