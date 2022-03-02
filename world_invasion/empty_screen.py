import sys
import pygame

screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption('Empty Window')
screen.fill((125,200,100))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit() 
        elif event.type == pygame.KEYDOWN:
            print(event.key)
            if event.key == pygame.K_RIGHT:
                print('right pressed')
