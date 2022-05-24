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

    def __init__(self, window, SpriteSpeed, *groups):
        self.windowSize = window.get_size()[0]
        self.size = self.windowSize / 16
        self.speed = SpriteSpeed
        self.direction = RIGHT
        self.bodies = []
        self.bodyDirections = []
        self.bodyWait = int(self.size // SpriteSpeed)
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

        self.bodyDirections.insert(0, self.direction)

    def bodyInstructions(self):
        body: SnakeBody
        for num, body in enumerate(self.bodies):
            num += 1
            body.move(self.bodyDirections[num * self.bodyWait - 1])

    def appleEaten(self):
        self.score += 1
        if len(self.bodies) == 0:
            sprite = SnakeBody(self.size, self.speed, self.rect.x, self.rect.y)
            sprite.first = True
            self.bodies.append(sprite)
        else:
            body = self.bodies[-1]
            sprite = SnakeBody(self.size, self.speed, body.rect.x, body.rect.y)
            self.bodies.append(sprite)

    def checkDeath(self):
        windowSize = self.windowSize
        border = windowSize / 20

        if any([border > coord or windowSize - border - self.size < coord for coord in (self.rect.x, self.rect.y)]):
            return True

        if len(self.bodies) < 1:
            return False

        changePos = self.size * 1 / 6
        newSize = self.size * 2 / 3

        newRect = pygame.Rect(self.rect.x + changePos, self.rect.y + changePos, newSize, newSize)

        for body in [sprite for sprite in self.bodies if sprite.age > sprite.ageNeeded]:
            if newRect.colliderect(body.rect):
                return True

        return False

    def appleTouch(self, apple):
        if self.rect.colliderect(apple):
            return True
        for body in self.bodies:
            if body.rect.colliderect:
                return True
        return False


class SnakeBody(Sprite):
    first = False

    def __init__(self, SpriteSize, SpriteSpeed, xCood, yCoord, *groups):
        self.size = SpriteSize
        self.speed = SpriteSpeed
        self.age = 1
        self.ageNeeded = int(SpriteSize // SpriteSpeed)
        self.image = pygame.Surface([SpriteSize, SpriteSize])
        pygame.draw.rect(self.image, (130, 0, 184), pygame.Rect(0, 0, SpriteSize, SpriteSize))
        self.rect = self.image.get_rect()
        self.rect.x = xCood
        self.rect.y = yCoord

        super().__init__(*groups)

    def move(self, direction):
        if self.age + self.first > self.ageNeeded:
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
        self.windowSize = window.get_size()[0]
        self.size = self.size = self.windowSize / 32
        self.image = pygame.Surface([self.size, self.size])
        pygame.draw.rect(self.image, (255, 0, 0), pygame.Rect(0, 0, self.size, self.size))
        self.rect = self.image.get_rect()
        super().__init__(*groups)
        self.randomizePos()

    def randomizePos(self):
        self.rect.x = randint(self.windowSize / 20, self.windowSize * 0.95 - self.size)
        self.rect.y = randint(self.windowSize / 20, self.windowSize * 0.95 - self.size)
