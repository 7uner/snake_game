import pygame
import random
import time

class Snake:
    def __init__(self, gameWindow, colors, snake_size=20, speed=15):
        self.SNAKE_SIZE = snake_size
        self.speed = speed
        self.win = gameWindow

        # Colors
        self.color = colors

        # Initialize Pygame
        pygame.init()

        # Snake settings
        self.snake_pos = [[100, 60], [80, 60], [60, 60]]
        self.snake_direction = 'RIGHT'
        self.change_to = self.snake_direction

    def draw_snake(self):
        for pos in self.snake_pos:
            pygame.draw.rect(self.win, self.color, pygame.Rect(pos[0], pos[1], self.SNAKE_SIZE, self.SNAKE_SIZE))

    def direction_event_handler(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if self.change_to != 'DOWN':
                        self.change_to = 'UP'
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if self.change_to != 'UP':
                        self.change_to = 'DOWN'
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if self.change_to != 'RIGHT':
                        self.change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if self.change_to != 'LEFT':
                        self.change_to = 'RIGHT'

        if self.change_to == 'UP':
            self.snake_direction = 'UP'
        if self.change_to == 'DOWN':
            self.snake_direction = 'DOWN'
        if self.change_to == 'LEFT':
            self.snake_direction = 'LEFT'
        if self.change_to == 'RIGHT':
            self.snake_direction = 'RIGHT'

    def move_snake(self):
        new_head = list(self.snake_pos[0])
        if self.snake_direction == 'UP':
            new_head[1] -= self.SNAKE_SIZE
        if self.snake_direction == 'DOWN':
            new_head[1] += self.SNAKE_SIZE
        if self.snake_direction == 'LEFT':
            new_head[0] -= self.SNAKE_SIZE
        if self.snake_direction == 'RIGHT':
            new_head[0] += self.SNAKE_SIZE

        self.snake_pos.insert(0, new_head)

