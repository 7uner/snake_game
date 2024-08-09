import pygame
import random
import time

class SnakeGame:
    def __init__(self, colors, width, height, snake_size=20, speed=15):
        # Game settings
        self.WIDTH = width
        self.HEIGHT = height
        self.SNAKE_SIZE = snake_size
        self.speed = speed
        self.score = 0

        # Colors
        self.WHITE, self.BLACK, self.RED, self.GREEN = colors

        # Initialize Pygame
        pygame.init()
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()

        # Snake settings
        self.snake_pos = [[100, 50], [80, 50], [60, 50]]
        self.snake_direction = 'RIGHT'
        self.change_to = self.snake_direction

        # Food settings
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
        time.sleep(2)  # Use time.sleep instead of pygame.time.sleep
        pygame.quit()
        quit()

    def draw_snake(self):
        for pos in self.snake_pos:
            pygame.draw.rect(self.win, self.GREEN, pygame.Rect(pos[0], pos[1], self.SNAKE_SIZE, self.SNAKE_SIZE))

    def draw_food(self):
        pygame.draw.rect(self.win, self.RED, pygame.Rect(self.food_pos[0], self.food_pos[1], self.SNAKE_SIZE, self.SNAKE_SIZE))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
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

            # Update the direction of the snake
            if self.change_to == 'UP':
                self.snake_direction = 'UP'
            if self.change_to == 'DOWN':
                self.snake_direction = 'DOWN'
            if self.change_to == 'LEFT':
                self.snake_direction = 'LEFT'
            if self.change_to == 'RIGHT':
                self.snake_direction = 'RIGHT'

            # Move the snake
            if self.snake_direction == 'UP':
                self.snake_pos[0][1] -= self.SNAKE_SIZE
            if self.snake_direction == 'DOWN':
                self.snake_pos[0][1] += self.SNAKE_SIZE
            if self.snake_direction == 'LEFT':
                self.snake_pos[0][0] -= self.SNAKE_SIZE
            if self.snake_direction == 'RIGHT':
                self.snake_pos[0][0] += self.SNAKE_SIZE

            # Snake body growing mechanism
            self.snake_pos.insert(0, list(self.snake_pos[0]))
            if self.snake_pos[0] == self.food_pos:
                self.score += 1
                self.food_spawn = False
            else:
                self.snake_pos.pop()

            if not self.food_spawn:
                self.food_pos = self.random_food_position()
            self.food_spawn = True

            # Fill background
            self.win.fill(self.BLACK)

            # Draw snake
            self.draw_snake()

            # Draw food
            self.draw_food()

            # Game Over conditions
            if self.snake_pos[0][0] < 0 or self.snake_pos[0][0] > (self.WIDTH - self.SNAKE_SIZE):
                self.game_over()
            if self.snake_pos[0][1] < 0 or self.snake_pos[0][1] > (self.HEIGHT - self.SNAKE_SIZE):
                self.game_over()

            for block in self.snake_pos[1:]:
                if self.snake_pos[0] == block:
                    self.game_over()

            # Refresh game screen
            pygame.display.update()

            # Frame Per Second /Refresh Rate
            self.clock.tick(self.speed)
