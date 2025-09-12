'''
Maak het plaatje dat in dit mapje staat na.

Slides: 
https://docs.google.com/presentation/d/1YwoUdeWABUYJkSfNzzZzDbCKvCVmWoo9Z5Uu7f_Y_K4/edit?usp=sharing
'''
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Fake flappybird!')
clock = pygame.time.Clock()
running = True

surface = pygame.Surface((900, 400))
surface.fill("blue")

bird = pygame.Surface((25, 25))
bird.fill("yellow")

paarse_dildo_1 = pygame.Surface((50, 200))
paarse_dildo_1.fill("green")

paarse_dildo_2 = pygame.Surface((50, 100))
paarse_dildo_2.fill("green")

paarse_dildo_3 = pygame.Surface((50, 100))
paarse_dildo_3.fill("green")

paarse_dildo_4 = pygame.Surface((50, 500))
paarse_dildo_4.fill("green")

while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.blit(surface, (0, 0))
  screen.blit(bird, (50, 200))
  screen.blit(paarse_dildo_1, (150, 0))
  screen.blit(paarse_dildo_2, (150, 300))
  screen.blit(paarse_dildo_3, (300, 0))
  screen.blit(paarse_dildo_4, (300, 150))

  pygame.display.update()
  clock.tick(60)
