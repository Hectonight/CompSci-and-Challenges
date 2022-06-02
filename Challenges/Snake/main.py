from pygame.time import Clock
from pygame.locals import *
from pygame.draw import *
from GameObjects import *

import pygame
import time
import sys

# setup
pygame.init()


def draw():
    window.fill((102, 237, 90))
    walls_chunk = size / 20
    green = (78, 158, 71)
    rect(window, green, pygame.Rect(walls_chunk, walls_chunk, round(size * 0.9), round(size * 0.9)))


size = 800

pygame.display.set_caption('Snake')
window = pygame.display.set_mode((size, size))
draw()
pygame.display.flip()

sprite_list = pygame.sprite.Group()

clock = Clock()
speed = 4
head = SnakeHead(window, speed)
coord = 15 * size / 32
head.rect.x = coord
head.rect.y = coord

sprite_list.add(head)
sprite_list.draw(window)

started = False
apple_eaten = False
alive = True
count = 0
apple = None

# main game loop
while alive:
    for event in pygame.event.get():

        # Quit
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key in [K_LEFT, K_a]:
                started = True
                head.direction = LEFT

            elif event.key in [K_RIGHT, K_d]:
                started = True
                head.direction = RIGHT

            elif event.key in [K_UP, K_w]:
                started = True
                head.direction = UP

            elif event.key in [K_DOWN, K_s]:
                started = True
                head.direction = DOWN

            if event.key == K_g:
                apple_eaten = True

    if started:
        if apple_eaten:
            head.apple_eaten()
            apple_eaten = False
        head.move()
        head.body_instructions()
        alive = not head.check_death()
        if apple not in sprite_list:
            count += 1
            if count == 20:
                count = 0
                apple = Apple(window)
                sprite_list.add(apple)

        elif head.rect.colliderect(apple):
            sprite_list.remove(apple)
            head.apple_eaten()

    clock.tick(60)
    draw()
    for sprite in set(head.bodies) - set(sprite_list):
        sprite_list.add(sprite)
    sprite_list.draw(window)
    pygame.display.flip()

print(f"You got a score of {head.score}")
