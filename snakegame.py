import pygame
import random
import time
import sys

class SnakeGame:
    def __init__(self, colors, width, height, snake_size=20, speed=15):
        self.WIDTH = width
        self.HEIGHT = height
        self.SNAKE_SIZE = snake_size
        self.speed = speed
        self.score = 0

        self.WHITE, self.BLACK, self.RED, self.GREEN = colors

        pygame.init()
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()

        self.snake_pos = [[100, 60], [80, 60], [60, 60]]
        self.snake_direction = 'RIGHT'
        self.change_to = self.snake_direction

        self.food_pos = self.random_food_position()
        self.food_spawn = True

    def random_food_position(self):
        return [random.randrange(1, (self.WIDTH // self.SNAKE_SIZE)) * self.SNAKE_SIZE,
                random.randrange(1, (self.HEIGHT // self.SNAKE_SIZE)) * self.SNAKE_SIZE]

    def game_over(self):
        font = pygame.font.SysFont('times new roman', 50)
        GO_surf = font.render('Your Score is : ' + str(self.score), True, self.RED)
        GO_rect = GO_surf.get_rect()
        GO_rect.midtop = (self.WIDTH / 2, self.HEIGHT / 4)
        self.win.blit(GO_surf, GO_rect)
        pygame.display.flip()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    def draw_snake(self):
        for pos in self.snake_pos:
            pygame.draw.rect(self.win, self.GREEN, pygame.Rect(pos[0], pos[1], self.SNAKE_SIZE, self.SNAKE_SIZE))

    def draw_food(self):
        pygame.draw.rect(self.win, self.RED, pygame.Rect(self.food_pos[0], self.food_pos[1], self.SNAKE_SIZE, self.SNAKE_SIZE))

    def draw_grid(self):
        for i in range(self.WIDTH // self.SNAKE_SIZE):
            pygame.draw.line(self.win, self.WHITE, (i * self.SNAKE_SIZE, 0),
                             (i * self.SNAKE_SIZE, self.HEIGHT))
        for i in range(self.HEIGHT // self.SNAKE_SIZE):
            pygame.draw.line(self.win, self.WHITE, (0, i * self.SNAKE_SIZE),
                             (self.WIDTH, i * self.SNAKE_SIZE))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
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

            if self.snake_pos[0] == self.food_pos:
                self.score += 1
                self.food_spawn = False
            else:
                self.snake_pos.pop()

            if not self.food_spawn:
                self.food_pos = self.random_food_position()
            self.food_spawn = True

            print(self.snake_pos[0])
            self.win.fill(self.BLACK)

            self.draw_grid()
            self.draw_snake()
            self.draw_food()

            if (self.snake_pos[0][0] < 0 or self.snake_pos[0][0] >= self.WIDTH or
                self.snake_pos[0][1] < 0 or self.snake_pos[0][1] >= self.HEIGHT):
                self.game_over()

            for block in self.snake_pos[1:]:
                if self.snake_pos[0] == block:
                    self.game_over()

            pygame.display.update()
            self.clock.tick(self.speed)
