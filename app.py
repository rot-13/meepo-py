import pygame
import os
from time import sleep

#Colours
WHITE = (255,255,255)

os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()
lcd = pygame.display.set_mode((320, 240))
pygame.mouse.set_visible(False)
lcd.fill((0,0,0))
pygame.display.update()

font_big = pygame.font.Font(None, 100)

running = True
k = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    k += 1
    lcd.fill((0,0,0))
    text_surface = font_big.render('%d'%k, True, WHITE)
    rect = text_surface.get_rect(center=(160,120))
    lcd.blit(text_surface, rect)
    pygame.display.update()
    sleep(1)
pygame.quit()
