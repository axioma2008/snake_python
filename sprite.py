import pygame
from settings import *
import random


class Snake(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.direction = "UP"
        self.image_directions = {"UP": pygame.image.load("images/snake_up.png"),
                                 "DOWN": pygame.image.load("images/snake_down.png"),
                                 "LEFT": pygame.image.load("images/snake_left.png"),
                                 "RIGHT": pygame.image.load("images/snake_right.png")}
        self.image = self.image_directions[self.direction]
        self.rect = self.image.get_rect()
        self.rect.y = HEIGHT // 2 - self.rect.height // 2
        self.rect.x = WIDTH // 2 - self.rect.width // 2
        self.apples_counter = 0
        self.tail_group = pygame.sprite.Group()
        self.prev_tail_pos = self.rect.center

    def update(self) -> None:
        self.prev_tail_pos = self.rect.center
        if self.direction == "UP":
            self.rect.y -= 1

        elif self.direction == "DOWN":
            self.rect.y += 1

        elif self.direction == "RIGHT":
            self.rect.x += 1

        elif self.direction == "LEFT":
            self.rect.x -= 1
        for sprite in self.tail_group:
            next_pos = sprite.rect.center
            sprite.move(self.prev_tail_pos)
            self.prev_tail_pos = next_pos

    def change_direction(self, new_direction):
        if self.direction != new_direction:
            self.image = self.image_directions[new_direction]
            self.direction = new_direction

    def add_tail(self):
        self.apples_counter += 1
        tail_pos = []
        if self.tail_group.sprites():
            now_tail_pos = self.tail_group.sprites()[-1].rect.center
        else:
            now_tail_pos = self.rect.center
        x_movement = self.prev_tail_pos[0] - now_tail_pos[0]
        y_movement = self.prev_tail_pos[1] - now_tail_pos[1]
        if x_movement < 0:
            tail_pos = [now_tail_pos[0] - 27, now_tail_pos[1]]
        elif x_movement > 0:
            tail_pos = [now_tail_pos[0] + 27, now_tail_pos[1]]
        elif y_movement > 0:
            tail_pos = [now_tail_pos[0], now_tail_pos[1] + 27]
        elif y_movement < 0:
            tail_pos = [now_tail_pos[0], now_tail_pos[1] - 27]

        tail = SnakeTail(tail_pos)
        print(self.tail_group.sprites()[:1])
        self.tail_group.add(tail)


class Apple(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/apple.png")
        self.rect = self.image.get_rect()

        self.rect.x = random.randint(0, WIDTH - self.rect.height)
        self.rect.y = random.randint(0, HEIGHT - self.rect.height)


class SnakeTail(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/tale.png")
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def move(self, pos):
        self.rect.center = pos





