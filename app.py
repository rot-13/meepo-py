import pygame
import os
from time import sleep
import requests

#Colours
WHITE = (255,255,255)

os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()
lcd = pygame.display.set_mode((320, 240), pygame.FULLSCREEN)
pygame.mouse.set_visible(False)
lcd.fill((0,0,0))
pygame.display.update()

font_medium = pygame.font.Font(None, 30)

running = True
k = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    r = requests.get("https://meepo-api.herokuapp.com/people")
    people_str = "";
    for person in r.json()['people']:
        people_str += person['name'] + ', '

    k += 1
    lcd.fill((0,0,0))
    text_surface = font_medium.render(people_str, True, WHITE)
    rect = text_surface.get_rect(center=(160,120))
    lcd.blit(text_surface, rect)
    pygame.display.update()
    sleep(1)
pygame.quit()
