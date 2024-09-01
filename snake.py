import pygame


class Snake:
    def __init__(self, gameWindow, colors, snake_pos, snake_direction, snake_size=20, speed=15):
        self.SNAKE_SIZE = snake_size
        self.speed = speed
        self.win = gameWindow

        # Colors
        self.color = colors

        # Initialize Pygame
        pygame.init()

        # Snake settings
        self.snake_pos = snake_pos
        self.snake_direction = snake_direction

    def draw_snake(self):
        for pos in self.snake_pos:
            pygame.draw.rect(self.win, self.color, pygame.Rect(pos[0], pos[1], self.SNAKE_SIZE, self.SNAKE_SIZE))

    def direction_event_handler(self, events, player=1):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if player == 1:
                    if event.key == pygame.K_UP:
                        if self.snake_direction != 'DOWN':
                            self.snake_direction = 'UP'
                    elif event.key == pygame.K_DOWN:
                        if self.snake_direction != 'UP':
                            self.snake_direction = 'DOWN'
                    elif event.key == pygame.K_LEFT:
                        if self.snake_direction != 'RIGHT':
                            self.snake_direction = 'LEFT'
                    elif event.key == pygame.K_RIGHT:
                        if self.snake_direction != 'LEFT':
                            self.snake_direction = 'RIGHT'
                elif player == 2:
                    if event.key == pygame.K_w:
                        if self.snake_direction != 'DOWN':
                            self.snake_direction = 'UP'
                    elif event.key == pygame.K_s:
                        if self.snake_direction != 'UP':
                            self.snake_direction = 'DOWN'
                    elif event.key == pygame.K_a:
                        if self.snake_direction != 'RIGHT':
                            self.snake_direction = 'LEFT'
                    elif event.key == pygame.K_d:
                        if self.snake_direction != 'LEFT':
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

