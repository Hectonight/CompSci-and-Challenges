import email.errors
import random

from pygame.sprite import Sprite
from random import randint
import pygame

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3


class SnakeHead(Sprite):

    def __init__(self, window, sprite_speed, *groups):
        self.window_size = window.get_size()[0]
        self.size = self.window_size / 16
        self.speed = sprite_speed
        self.direction = RIGHT
        self.bodies = []
        self.body_directions = []
        self.body_wait = int(self.size // sprite_speed)
        self.image = pygame.Surface([self.size, self.size])
        pygame.draw.rect(self.image, (234, 0, 255), pygame.Rect(0, 0, self.size, self.size))
        self.rect = self.image.get_rect()
        self.score = 0

        super().__init__(*groups)

    def move(self):
        if self.direction == LEFT:
            self.rect.x -= self.speed
        elif self.direction == RIGHT:
            self.rect.x += self.speed
        elif self.direction == UP:
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

        self.body_directions.insert(0, self.direction)

    def body_instructions(self):
        body: SnakeBody
        for num, body in enumerate(self.bodies):
            num += 1
            body.move(self.body_directions[num * self.body_wait - 1])

    def apple_eaten(self):
        self.score += 1
        if len(self.bodies) == 0:
            sprite = SnakeBody(self.size, self.speed, self.rect.x, self.rect.y)
            sprite.first = True
            self.bodies.append(sprite)
        else:
            body = self.bodies[-1]
            sprite = SnakeBody(self.size, self.speed, body.rect.x, body.rect.y)
            self.bodies.append(sprite)

    def check_death(self):
        window_size = self.window_size
        border = window_size / 20

        if any([border > coord or window_size - border - self.size < coord for coord in (self.rect.x, self.rect.y)]):
            return True

        if len(self.bodies) < 1:
            return False

        change_position = self.size * 1 / 6
        new_size = self.size * 2 / 3

        new_rect = pygame.Rect(self.rect.x + change_position, self.rect.y + change_position, new_size, new_size)

        for body in [sprite for sprite in self.bodies if sprite.age > sprite.age_needed]:
            if new_rect.colliderect(body.rect):
                return True

        return False

    def apple_touch(self, apple):
        if self.rect.colliderect(apple):
            return True
        for body in self.bodies:
            if body.rect.colliderect:
                return True
        return False


class SnakeBody(Sprite):
    first = False

    def __init__(self, sprite_size, sprite_speed, xCoord, yCoord, *groups):
        self.size = sprite_size
        self.speed = sprite_speed
        self.age = 1
        self.age_needed = int(sprite_size // sprite_speed)
        self.image = pygame.Surface([sprite_size, sprite_size])
        pygame.draw.rect(self.image, (130, 0, 184), pygame.Rect(0, 0, sprite_size, sprite_size))
        self.rect = self.image.get_rect()
        self.rect.x = xCoord
        self.rect.y = yCoord

        super().__init__(*groups)

    def move(self, direction):
        if self.age + self.first > self.age_needed:
            if direction == LEFT:
                self.rect.x -= self.speed
            elif direction == RIGHT:
                self.rect.x += self.speed
            elif direction == UP:
                self.rect.y -= self.speed
            else:
                self.rect.y += self.speed
        else:
            self.age += 1


class Apple(Sprite):

    def __init__(self, window, *groups):
        self.window_size = window.get_size()[0]
        self.size = self.size = self.window_size / 32
        self.image = pygame.Surface([self.size, self.size])
        pygame.draw.rect(self.image, (255, 0, 0), pygame.Rect(0, 0, self.size, self.size))
        self.rect = self.image.get_rect()
        super().__init__(*groups)
        self.randomize_position()

    def randomize_position(self):
        self.rect.x = randint(self.window_size / 20, self.window_size * 0.95 - self.size)
        self.rect.y = randint(self.window_size / 20, self.window_size * 0.95 - self.size)
