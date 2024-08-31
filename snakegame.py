import pygame
import random
import time
import sys

class Snake:
    def __init__(self, win, color, snake_size=20, speed=15, start_pos=[[100, 60], [80, 60], [60, 60]], direction='RIGHT'):
        self.win = win
        self.color = color
        self.SNAKE_SIZE = snake_size
        self.speed = speed
        self.snake_pos = start_pos
        self.snake_direction = direction
        self.change_to = self.snake_direction

    def direction_event_handler(self, events, player=1):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if player == 1:
                    if event.key == pygame.K_UP and self.snake_direction != 'DOWN':
                        self.change_to = 'UP'
                    elif event.key == pygame.K_DOWN and self.snake_direction != 'UP':
                        self.change_to = 'DOWN'
                    elif event.key == pygame.K_LEFT and self.snake_direction != 'RIGHT':
                        self.change_to = 'LEFT'
                    elif event.key == pygame.K_RIGHT and self.snake_direction != 'LEFT':
                        self.change_to = 'RIGHT'
                elif player == 2:
                    if event.key == pygame.K_w and self.snake_direction != 'DOWN':
                        self.change_to = 'UP'
                    elif event.key == pygame.K_s and self.snake_direction != 'UP':
                        self.change_to = 'DOWN'
                    elif event.key == pygame.K_a and self.snake_direction != 'RIGHT':
                        self.change_to = 'LEFT'
                    elif event.key == pygame.K_d and self.snake_direction != 'LEFT':
                        self.change_to = 'RIGHT'

    def move_snake(self):
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

    def draw_snake(self):
        for pos in self.snake_pos:
            pygame.draw.rect(self.win, self.color, pygame.Rect(pos[0], pos[1], self.SNAKE_SIZE, self.SNAKE_SIZE))


class SnakeGame:
    def __init__(self, colors, width, height, snake_size=20, speed=15):
        self.WIDTH = width
        self.HEIGHT = height
        self.score1 = 0
        self.score2 = 0

        self.WHITE, self.BLACK, self.RED, self.GREEN, self.BLUE = colors

        pygame.init()
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Multiplayer Snake Game")
        self.clock = pygame.time.Clock()

        self.food_pos = self.random_food_position(snake_size)
        self.food_spawn = True

    def random_food_position(self, SNAKE_SIZE):
        return [random.randrange(1, (self.WIDTH // SNAKE_SIZE)) * SNAKE_SIZE,
                random.randrange(1, (self.HEIGHT // SNAKE_SIZE)) * SNAKE_SIZE]

    def game_over(self):
        font = pygame.font.SysFont('times new roman', 50)
        GO_surf = font.render(f'Player 1 Score: {self.score1}, Player 2 Score: {self.score2}', True, self.RED)
        GO_rect = GO_surf.get_rect()
        GO_rect.midtop = (self.WIDTH / 2, self.HEIGHT / 4)
        self.win.blit(GO_surf, GO_rect)
        pygame.display.flip()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    def draw_food(self, SNAKE_SIZE):
        pygame.draw.rect(self.win, self.RED, pygame.Rect(self.food_pos[0], self.food_pos[1], SNAKE_SIZE, SNAKE_SIZE))

    def draw_grid(self, SNAKE_SIZE=20):
        for i in range(self.WIDTH // SNAKE_SIZE):
            pygame.draw.line(self.win, self.WHITE, (i * SNAKE_SIZE, 0), (i * SNAKE_SIZE, self.HEIGHT))
        for i in range(self.HEIGHT // SNAKE_SIZE):
            pygame.draw.line(self.win, self.WHITE, (0, i * SNAKE_SIZE), (self.WIDTH, i * SNAKE_SIZE))

    def run(self):
        snake1 = Snake(self.win, self.GREEN)
        snake2 = Snake(self.win, self.BLUE, start_pos=[[300, 300], [280, 300], [260, 300]], direction='LEFT')

        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            snake1.direction_event_handler(events, player=1)
            snake2.direction_event_handler(events, player=2)

            snake1.move_snake()
            snake2.move_snake()

            if snake1.snake_pos[0] == self.food_pos:
                self.score1 += 1
                self.food_spawn = False
            else:
                snake1.snake_pos.pop()

            if snake2.snake_pos[0] == self.food_pos:
                self.score2 += 1
                self.food_spawn = False
            else:
                snake2.snake_pos.pop()

            if not self.food_spawn:
                self.food_pos = self.random_food_position(20)
            self.food_spawn = True

            self.win.fill(self.BLACK)

            self.draw_grid()
            snake1.draw_snake()
            snake2.draw_snake()
            self.draw_food(20)

            if (snake1.snake_pos[0][0] < 0 or snake1.snake_pos[0][0] >= self.WIDTH or
                snake1.snake_pos[0][1] < 0 or snake1.snake_pos[0][1] >= self.HEIGHT or
                snake2.snake_pos[0][0] < 0 or snake2.snake_pos[0][0] >= self.WIDTH or
                snake2.snake_pos[0][1] < 0 or snake2.snake_pos[0][1] >= self.HEIGHT):
                self.game_over()

            for block in snake1.snake_pos[1:]:
                if snake1.snake_pos[0] == block or snake2.snake_pos[0] == block:
                    self.game_over()

            for block in snake2.snake_pos[1:]:
                if snake1.snake_pos[0] == block or snake2.snake_pos[0] == block:
                    self.game_over()

            pygame.display.update()
            self.clock.tick(snake1.speed)
